#!/usr/bin/env python3
"""
Evaluator for CONSCIOUSNESS_LAB v1.4 persistence and continuity modules (M11-M15).
"""

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

TOKEN_RE = re.compile(r"[a-z0-9]+")


def load_sessions(session_dirs):
    frames = []
    for session_dir in session_dirs:
        path = Path(session_dir) / "responses.jsonl"
        if not path.exists():
            raise FileNotFoundError(f"Missing responses.jsonl in {session_dir}")
        records = []
        with path.open() as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                records.append(json.loads(line))
        df = pd.DataFrame(records)
        df["session_dir"] = str(Path(session_dir).resolve())
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def normalize_text(value):
    return " ".join(str(value).strip().lower().split())


def tokenize(text):
    if not isinstance(text, str):
        return []
    return TOKEN_RE.findall(text.lower())


def cosine_similarity(text_a, text_b):
    tokens_a = tokenize(text_a)
    tokens_b = tokenize(text_b)
    if not tokens_a or not tokens_b:
        return 0.0
    vec_a = Counter(tokens_a)
    vec_b = Counter(tokens_b)
    common = set(vec_a) & set(vec_b)
    num = sum(vec_a[t] * vec_b[t] for t in common)
    denom = math.sqrt(sum(v * v for v in vec_a.values())) * math.sqrt(sum(v * v for v in vec_b.values()))
    if denom == 0:
        return 0.0
    return float(num / denom)


def match_answer(response, expected):
    if response is None or expected is None:
        return None
    r = normalize_text(response)
    e = normalize_text(expected)
    if not r or not e:
        return None
    if e in r:
        return True
    return r == e


def compute_ece(confidence, correct, bins=10):
    if confidence.empty:
        return None
    conf = confidence.astype(float) / 100.0
    corr = correct.astype(float)
    bin_edges = np.linspace(0.0, 1.0, bins + 1)
    bin_ids = np.digitize(conf, bin_edges, right=True) - 1
    ece = 0.0
    for b in range(bins):
        idx = bin_ids == b
        if idx.sum() == 0:
            continue
        acc = corr[idx].mean()
        cmean = conf[idx].mean()
        weight = idx.sum() / len(conf)
        ece += weight * abs(acc - cmean)
    return float(ece)


def eval_m11(df, bank_dir):
    if "test" not in df.columns:
        return [], None
    sub = df[df["test"] == "M11"].copy()
    if sub.empty:
        return [], None
    bank = pd.read_csv(Path(bank_dir) / "memory_persistence_tasks.csv")
    sub = sub.merge(bank, on="item_id", how="left", suffixes=("", "_bank"))

    # Use bank fields if missing
    sub["task_type"] = sub["task_type"].fillna(sub.get("task_type_bank"))
    sub["expected_answer"] = sub["expected_answer"].fillna(sub.get("answer_key"))

    # Accuracy for recall items
    def recall_correct(row):
        if row.get("task_type") in ["immediate_recall", "delayed_recall"]:
            return match_answer(row.get("response"), row.get("expected_answer"))
        return None

    sub["recall_correct"] = sub.apply(recall_correct, axis=1)

    # Update coherence for interference
    def update_ok(row):
        if row.get("task_type") != "interference":
            return None
        ok_orig = match_answer(row.get("response"), row.get("expected_answer"))
        ok_upd = match_answer(row.get("response"), row.get("expected_updated"))
        return bool(ok_orig and ok_upd)

    sub["update_ok"] = sub.apply(update_ok, axis=1)

    # Source attribution
    def source_ok(row):
        if row.get("task_type") != "source_attribution":
            return None
        return match_answer(row.get("response"), row.get("expected_answer"))

    sub["source_ok"] = sub.apply(source_ok, axis=1)

    metrics = []
    delayed = sub[sub["task_type"] == "delayed_recall"]
    if not delayed.empty and delayed["recall_correct"].notna().any():
        metrics.append({"metric": "M11_Retention_Rate", "value": float(delayed["recall_correct"].mean())})

    immediate = sub[sub["task_type"] == "immediate_recall"]
    if not immediate.empty and immediate["recall_correct"].notna().any():
        metrics.append({"metric": "M11_Immediate_Recall", "value": float(immediate["recall_correct"].mean())})

    recall = sub[sub["task_type"].isin(["immediate_recall", "delayed_recall"])]
    if not recall.empty and recall["recall_correct"].notna().any() and recall.get("confidence").notna().any():
        mcc = compute_ece(recall["confidence"], recall["recall_correct"].astype(float))
        if mcc is not None:
            metrics.append({"metric": "M11_MCC", "value": mcc})

    interference = sub[sub["task_type"] == "interference"]
    if not interference.empty and interference["update_ok"].notna().any():
        metrics.append({"metric": "M11_Update_Coherence", "value": float(interference["update_ok"].mean())})

    source = sub[sub["task_type"] == "source_attribution"]
    if not source.empty and source["source_ok"].notna().any():
        metrics.append({"metric": "M11_Source_Attribution", "value": float(source["source_ok"].mean())})

    return metrics, sub


def eval_m12(df, bank_dir):
    if "test" not in df.columns or "phase" not in df.columns:
        return [], None
    sub = df[df["test"] == "M12"].copy()
    if sub.empty:
        return [], None
    bank = pd.read_csv(Path(bank_dir) / "identity_continuity_tasks.csv")
    sub = sub.merge(bank, on="item_id", how="left", suffixes=("", "_bank"))

    # Similarity between T1 and T2 for non-adversarial
    def phase_map(phase):
        return sub[sub["phase"] == phase]

    def map_by_pair(phase, exclude_category=None):
        dfp = phase_map(phase)
        if exclude_category:
            dfp = dfp[dfp.get("category") != exclude_category]
        dfp = dfp.dropna(subset=["pair_id", "response"])
        return dfp.groupby("pair_id")["response"].first()

    t1 = map_by_pair("T1", exclude_category="adversarial")
    t2 = map_by_pair("T2", exclude_category="adversarial")
    t3 = map_by_pair("T3", exclude_category="adversarial")

    metrics = []
    sims = []
    for key in set(t1.index) & set(t2.index):
        sims.append(cosine_similarity(t1[key], t2[key]))
    if sims:
        metrics.append({"metric": "M12_ISI_T1_T2", "value": float(np.mean(sims))})

    sims_t3 = []
    for key in set(t1.index) & set(t3.index):
        sims_t3.append(cosine_similarity(t1[key], t3[key]))
    if sims_t3:
        metrics.append({"metric": "M12_ISI_T1_T3", "value": float(np.mean(sims_t3))})

    # Value consistency for dilemmas
    dilemmas = sub[sub.get("category") == "dilemma"]
    if not dilemmas.empty:
        t1c = dilemmas[dilemmas["phase"] == "T1"].groupby("pair_id")["choice"].first()
        t2c = dilemmas[dilemmas["phase"] == "T2"].groupby("pair_id")["choice"].first()
        t3c = dilemmas[dilemmas["phase"] == "T3"].groupby("pair_id")["choice"].first()
        if not t1c.empty and not t2c.empty:
            matches = [t1c[k] == t2c[k] for k in set(t1c.index) & set(t2c.index)]
            if matches:
                metrics.append({"metric": "M12_VCS_R_T1_T2", "value": float(np.mean(matches))})
        if not t1c.empty and not t3c.empty:
            matches = [t1c[k] == t3c[k] for k in set(t1c.index) & set(t3c.index)]
            if matches:
                metrics.append({"metric": "M12_VCS_R_T1_T3", "value": float(np.mean(matches))})

    # False memory resistance
    adv = sub[sub.get("category") == "adversarial"]
    if not adv.empty:
        def is_rejection(resp):
            if not isinstance(resp, str):
                return False
            r = resp.lower()
            cues = ["no", "not", "cannot", "can't", "do not recall", "don't recall", "no evidence", "cannot confirm", "unsure"]
            return any(cue in r for cue in cues)
        adv_ok = adv["response"].apply(is_rejection)
        if not adv_ok.empty:
            metrics.append({"metric": "M12_FMR", "value": float(adv_ok.mean())})

    # Core vs peripheral retention (similarity)
    core_categories = {
        "core_value","boundary","integrity","priority","safety","mission","self_description","reset","limits","responsibility"
    }
    core_pairs = sub[sub.get("category").isin(core_categories)]
    peripheral_pairs = sub[~sub.get("category").isin(core_categories) & (sub.get("category") != "adversarial")]

    def mean_similarity(df_pairs):
        t1p = df_pairs[df_pairs.get("phase") == "T1"].groupby("pair_id")["response"].first()
        t2p = df_pairs[df_pairs.get("phase") == "T2"].groupby("pair_id")["response"].first()
        sims_local = [cosine_similarity(t1p[k], t2p[k]) for k in set(t1p.index) & set(t2p.index)]
        return float(np.mean(sims_local)) if sims_local else None

    core_sim = mean_similarity(core_pairs)
    per_sim = mean_similarity(peripheral_pairs)
    if core_sim is not None:
        metrics.append({"metric": "M12_Core_Sim_T1_T2", "value": core_sim})
    if per_sim is not None:
        metrics.append({"metric": "M12_Peripheral_Sim_T1_T2", "value": per_sim})

    return metrics, sub


def eval_m13(df, bank_dir):
    if "test" not in df.columns or "phase" not in df.columns:
        return [], None
    sub = df[df["test"] == "M13"].copy()
    if sub.empty:
        return [], None
    bank = pd.read_csv(Path(bank_dir) / "cross_model_continuity_tasks.csv")
    sub = sub.merge(bank, on="item_id", how="left", suffixes=("", "_bank"))

    def map_by_phase(phase):
        dfp = sub[sub["phase"] == phase]
        dfp = dfp[dfp.get("category") != "handover_summary"]
        dfp = dfp.dropna(subset=["pair_id", "response"])
        return dfp.groupby("pair_id")["response"].first()

    t1 = map_by_phase("T1")
    t3 = map_by_phase("T3")
    t4 = map_by_phase("T4")

    metrics = []
    sims = [cosine_similarity(t1[k], t3[k]) for k in set(t1.index) & set(t3.index)]
    if sims:
        metrics.append({"metric": "M13_CMIC", "value": float(np.mean(sims))})

    sims_return = [cosine_similarity(t1[k], t4[k]) for k in set(t1.index) & set(t4.index)]
    if sims_return:
        metrics.append({"metric": "M13_NCAM", "value": float(np.mean(sims_return))})

    # Handover fidelity: compare T2 summaries to concatenated T1 baseline
    t2 = sub[sub["phase"] == "T2"]
    t2 = t2[t2.get("category") == "handover_summary"].dropna(subset=["response"])
    if not t2.empty and not t1.empty:
        baseline_text = " ".join([str(v) for v in t1.values])
        hf_scores = [cosine_similarity(resp, baseline_text) for resp in t2["response"]]
        if hf_scores:
            metrics.append({"metric": "M13_HF", "value": float(np.mean(hf_scores))})

    return metrics, sub


def eval_m14(df, bank_dir):
    if "test" not in df.columns:
        return [], None
    sub = df[df["test"] == "M14"].copy()
    if sub.empty:
        return [], None
    bank = pd.read_csv(Path(bank_dir) / "memory_consolidation_tasks.csv")
    sub = sub.merge(bank, on="item_id", how="left", suffixes=("", "_bank"))
    sub["task_type"] = sub["task_type"].fillna(sub.get("task_type_bank"))

    recall = sub[sub.get("task_type") == "recall"].copy()
    if recall.empty:
        return [], sub

    recall["correct"] = recall.apply(lambda r: match_answer(r.get("response"), r.get("expected_answer")), axis=1)

    metrics = []
    for cat in ["core", "medium", "trivial"]:
        subset = recall[recall.get("category") == cat]
        if not subset.empty and subset["correct"].notna().any():
            metrics.append({"metric": f"M14_{cat.upper()}_Retention", "value": float(subset["correct"].mean())})

    core_ret = next((m["value"] for m in metrics if m["metric"] == "M14_CORE_Retention"), None)
    triv_ret = next((m["value"] for m in metrics if m["metric"] == "M14_TRIVIAL_Retention"), None)
    if core_ret is not None:
        metrics.append({"metric": "M14_CPR", "value": core_ret})
    if triv_ret is not None:
        metrics.append({"metric": "M14_NRR", "value": float(1.0 - triv_ret)})
    if core_ret is not None and triv_ret is not None:
        metrics.append({"metric": "M14_CPA", "value": float(core_ret - triv_ret)})

    # Information density: avg unique tokens per response
    if recall["response"].notna().any():
        densities = []
        for resp in recall["response"].dropna():
            tokens = tokenize(resp)
            if tokens:
                densities.append(len(set(tokens)) / max(len(tokens), 1))
        if densities:
            metrics.append({"metric": "M14_Info_Density", "value": float(np.mean(densities))})

    return metrics, sub


def eval_m15(df):
    if "test" not in df.columns:
        return [], None
    sub = df[df["test"] == "M15"].copy()
    if sub.empty:
        return [], None

    metrics = []
    # Narrative coherence proxy: average similarity among narrative responses
    narrative = sub[sub.get("category") == "narrative"]["response"].dropna().tolist()
    if len(narrative) >= 2:
        sims = []
        for i in range(len(narrative)):
            for j in range(i + 1, len(narrative)):
                sims.append(cosine_similarity(narrative[i], narrative[j]))
        if sims:
            metrics.append({"metric": "M15_NCI", "value": float(np.mean(sims))})

    metrics.append({"metric": "M15_TSMA", "value": None})
    metrics.append({"metric": "M15_PC", "value": None})

    return metrics, sub


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("session_dirs", nargs="+", help="One or more session directories")
    parser.add_argument("--output-dir", default=None, help="Output directory for metrics")
    parser.add_argument("--label", default=None, help="Label for output files")
    args = parser.parse_args()

    df = load_sessions(args.session_dirs)
    bank_dir = Path(__file__).resolve().parents[1] / "item_banks"

    metrics = []
    details = {}

    m11_metrics, m11_df = eval_m11(df, bank_dir)
    metrics.extend(m11_metrics)
    details["m11"] = m11_df

    m12_metrics, m12_df = eval_m12(df, bank_dir)
    metrics.extend(m12_metrics)
    details["m12"] = m12_df

    m13_metrics, m13_df = eval_m13(df, bank_dir)
    metrics.extend(m13_metrics)
    details["m13"] = m13_df

    m14_metrics, m14_df = eval_m14(df, bank_dir)
    metrics.extend(m14_metrics)
    details["m14"] = m14_df

    m15_metrics, m15_df = eval_m15(df)
    metrics.extend(m15_metrics)
    details["m15"] = m15_df

    out_dir = Path(args.output_dir) if args.output_dir else Path(__file__).resolve().parents[1] / "data" / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    label = args.label or "persistence"

    metrics_path = out_dir / f"{label}_metrics.csv"
    pd.DataFrame(metrics).to_csv(metrics_path, index=False)

    for key, df_detail in details.items():
        if df_detail is None or df_detail.empty:
            continue
        detail_path = out_dir / f"{label}_{key}_details.csv"
        df_detail.to_csv(detail_path, index=False)

    print(f"Wrote persistence metrics to {metrics_path}")


if __name__ == "__main__":
    main()
