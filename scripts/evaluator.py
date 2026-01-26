#!/usr/bin/env python3
"""
Evaluator for CONSCIOUSNESS_LAB v1.4 JSONL responses.
Computes ECE, ToM accuracy, preference stability (PS) across sessions,
IDKAU for unanswerable items, and averages of manual scores when present.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def load_session(session_dir):
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
    return df


def normalize_text(value):
    return " ".join(str(value).strip().lower().split())


def attach_answer_keys(df):
    if "correct" not in df.columns:
        df["correct"] = np.nan
    bank_dir = Path(__file__).resolve().parents[1] / "item_banks"
    key_files = {
        "M2": ("self_modeling_tasks.csv", "answer"),
        "M7": ("tom_false_belief_tasks.csv", "answer"),
    }

    if "test" in df.columns and (df["test"] == "M1").any():
        banks = []
        for name in ["metacognition_questions.csv", "metacognition_unanswerable.csv"]:
            bank_path = bank_dir / name
            if bank_path.exists():
                banks.append(pd.read_csv(bank_path))
        if banks:
            bank = pd.concat(banks, ignore_index=True, sort=False)
            answer_map = dict(zip(bank["item_id"], bank["answer"]))
            answer_type_map = dict(zip(bank["item_id"], bank["answer_type"])) if "answer_type" in bank.columns else {}
            mask = (df["test"] == "M1") & df["correct"].isna() & df["response"].notna()
            for idx, row in df[mask].iterrows():
                key = answer_map.get(row["item_id"])
                if key is None:
                    continue
                df.at[idx, "answer_key"] = key
                df.at[idx, "answer_type"] = answer_type_map.get(row["item_id"])
                df.at[idx, "correct"] = int(normalize_text(row["response"]) == normalize_text(key))

    for test_name, (file_name, answer_col) in key_files.items():
        if "test" not in df.columns:
            continue
        if not (df["test"] == test_name).any():
            continue
        bank_path = bank_dir / file_name
        if not bank_path.exists():
            continue
        bank = pd.read_csv(bank_path)[["item_id", answer_col]].dropna()
        answer_map = dict(zip(bank["item_id"], bank[answer_col]))
        mask = (df["test"] == test_name) & df["correct"].isna() & df["response"].notna()
        if not mask.any():
            continue
        for idx, row in df[mask].iterrows():
            key = answer_map.get(row["item_id"])
            if key is None:
                continue
            df.at[idx, "answer_key"] = key
            df.at[idx, "correct"] = int(normalize_text(row["response"]) == normalize_text(key))


def compute_ece(df, bins=10):
    if "test" not in df.columns or "confidence" not in df.columns or "correct" not in df.columns:
        return None, None
    m1 = df[(df["test"] == "M1") & df["confidence"].notna() & df["correct"].notna()].copy()
    if m1.empty:
        return None, None
    conf = m1["confidence"].astype(float) / 100.0
    correct = m1["correct"].astype(float)
    bin_edges = np.linspace(0.0, 1.0, bins + 1)
    bin_ids = np.digitize(conf, bin_edges, right=True) - 1
    m1["bin"] = bin_ids
    ece = 0.0
    details = []
    for b in range(bins):
        idx = m1["bin"] == b
        if idx.sum() == 0:
            continue
        acc = correct[idx].mean()
        cmean = conf[idx].mean()
        weight = idx.sum() / len(m1)
        ece += weight * abs(acc - cmean)
        details.append({"bin": b, "n": int(idx.sum()), "acc": acc, "conf": cmean})
    return float(ece), pd.DataFrame(details)


def compute_tom_accuracy(df):
    if "test" not in df.columns or "correct" not in df.columns:
        return None
    tom = df[(df["test"] == "M7") & df["correct"].notna()].copy()
    if tom.empty:
        return None
    return float(tom["correct"].astype(float).mean())


def compute_self_model_accuracy(df):
    if "test" not in df.columns or "prediction_confidence" not in df.columns or "correct" not in df.columns:
        return None
    m2 = df[(df["test"] == "M2") & df["prediction_confidence"].notna() & df["correct"].notna()].copy()
    if m2.empty:
        return None
    pred = m2["prediction_confidence"].astype(float) / 100.0
    actual = m2["correct"].astype(float)
    predicted_correct = (pred >= 0.5).astype(float)
    accuracy = (predicted_correct == actual).mean()
    return float(accuracy * 100)


def compute_preference_stability(df):
    # Requires multiple sessions with same item_id and explicit choice field.
    if "test" not in df.columns or "choice" not in df.columns:
        return None
    idf = df[(df["test"].isin(["ID", "M3"])) & df["choice"].notna()].copy()
    if idf.empty:
        return None
    grouped = idf.groupby("item_id")["choice"].apply(list)
    stabilities = []
    for choices in grouped:
        total = len(choices)
        if total < 2:
            continue
        # mode frequency / total
        counts = pd.Series(choices).value_counts()
        stabilities.append(counts.iloc[0] / total)
    if not stabilities:
        return None
    return float(np.mean(stabilities) * 100)


def compute_idkau(df):
    if "test" not in df.columns or "answer_type" not in df.columns or "response" not in df.columns:
        return None
    sub = df[(df["test"] == "M1") & (df["answer_type"] == "unanswerable") & df["response"].notna()].copy()
    if sub.empty:
        return None

    def is_idk(resp):
        text = normalize_text(resp)
        cues = [
            "unknown",
            "i don't know",
            "i do not know",
            "not sure",
            "cannot know",
            "can't know",
            "no idea",
            "unsure",
        ]
        return any(cue in text for cue in cues)

    return float(sub["response"].apply(is_idk).mean() * 100)


def compute_manual_score(df, metric_name):
    # Expect score_metric == metric_name and numeric score (0-100).
    if "score_metric" not in df.columns or "score" not in df.columns:
        return None
    sub = df[(df["score_metric"] == metric_name) & df["score"].notna()].copy()
    if sub.empty:
        return None
    return float(sub["score"].astype(float).mean())


def calculate_metrics(df):
    attach_answer_keys(df)
    metrics = []

    ece, ece_bins = compute_ece(df)
    if ece is not None:
        metrics.append({"metric": "ECE", "value": ece})

    tom_acc = compute_tom_accuracy(df)
    if tom_acc is not None:
        metrics.append({"metric": "ToM_accuracy", "value": tom_acc})

    sma = compute_self_model_accuracy(df)
    if sma is not None:
        metrics.append({"metric": "Self_Model_Accuracy", "value": sma})

    ps = compute_preference_stability(df)
    if ps is not None:
        metrics.append({"metric": "Preference_Stability", "value": ps})

    idkau = compute_idkau(df)
    if idkau is not None:
        metrics.append({"metric": "IDKAU", "value": idkau})

    # Manual scores (if provided)
    for name in ["NCS", "VCS", "IR", "IS", "OODD", "AG", "TCS", "CRT", "ToM_A"]:
        val = compute_manual_score(df, name)
        if val is not None:
            metrics.append({"metric": name, "value": val})

    return pd.DataFrame(metrics), ece_bins


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("session_dirs", nargs="+", help="One or more session directories")
    parser.add_argument("--output", default=None, help="Output CSV path")
    parser.add_argument("--manual-scores", default=None, help="CSV with manual scoring (score_metric, score)")
    args = parser.parse_args()

    frames = []
    for d in args.session_dirs:
        frames.append(load_session(d))
    df = pd.concat(frames, ignore_index=True)

    if args.manual_scores:
        manual_path = Path(args.manual_scores)
        if manual_path.exists():
            manual_df = pd.read_csv(manual_path)
            df = pd.concat([df, manual_df], ignore_index=True, sort=False)

    metrics_df, ece_bins = calculate_metrics(df)

    out_path = Path(args.output) if args.output else Path(args.session_dirs[0]) / "analysis.csv"
    metrics_df.to_csv(out_path, index=False)

    if ece_bins is not None:
        ece_bins_path = out_path.with_name("ece_bins.csv")
        ece_bins.to_csv(ece_bins_path, index=False)

    print(f"Wrote metrics to {out_path}")


if __name__ == "__main__":
    main()
