#!/usr/bin/env python3
"""
Post-process raw session outputs into data/processed with plots and summaries.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except Exception:
    plt = None

from evaluator import calculate_metrics, attach_answer_keys
from agent_utils import load_agent_name


def now_iso():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_jsonl(path):
    records = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return pd.DataFrame(records)


def write_summary_md(path, session_id, processed_at, agent_name, model_id, signature_info, metrics_df, counts):
    lines = []
    lines.append(f"# Session Summary: {session_id}")
    lines.append("")
    lines.append(f"Processed at: {processed_at}")
    lines.append(f"Agent name: {agent_name}")
    lines.append(f"Model ID: {model_id}")
    if signature_info:
        if signature_info["mismatched"] is None:
            lines.append(f"Signature coverage: {signature_info['compliance']:.2%}")
            lines.append(f"Signature missing: {signature_info['missing']}")
        else:
            lines.append(f"Signature compliance: {signature_info['compliance']:.2%}")
            lines.append(f"Signature missing: {signature_info['missing']}")
            lines.append(f"Signature mismatched: {signature_info['mismatched']}")
    lines.append("")
    lines.append("## Metrics")
    if metrics_df.empty:
        lines.append("- None")
    else:
        for _, row in metrics_df.iterrows():
            value = row["value"]
            if isinstance(value, (float, np.floating)):
                lines.append(f"- {row['metric']}: {value:.4f}")
            else:
                lines.append(f"- {row['metric']}: {value}")
    lines.append("")
    lines.append("## Response Coverage")
    if counts.empty:
        lines.append("- None")
    else:
        for test, count in counts.items():
            lines.append(f"- {test}: {int(count)}")
    path.write_text("\n".join(lines))


def resolve_agent_name(metadata_path, responses_df):
    name = None
    if metadata_path.exists():
        meta = json.loads(metadata_path.read_text())
        name = meta.get("agent_name") or meta.get("signature")
    if not name and "agent_name" in responses_df.columns:
        unique = responses_df["agent_name"].dropna().unique()
        if len(unique) == 1:
            name = unique[0]
        elif len(unique) > 1:
            name = "MULTIPLE"
    if not name and "signature" in responses_df.columns:
        unique = responses_df["signature"].dropna().unique()
        if len(unique) == 1:
            name = unique[0]
        elif len(unique) > 1:
            name = "MULTIPLE"
    if not name:
        name = load_agent_name()
    return name or "UNKNOWN"


def resolve_model_id(metadata_path, responses_df):
    model_id = None
    if metadata_path.exists():
        meta = json.loads(metadata_path.read_text())
        model_id = meta.get("model_id")
    if not model_id and "model_id" in responses_df.columns:
        unique = responses_df["model_id"].dropna().unique()
        if len(unique) == 1:
            model_id = unique[0]
        elif len(unique) > 1:
            model_id = "MULTIPLE"
    return model_id or "UNKNOWN"


def signature_stats(responses_df, agent_name):
    if "signature" not in responses_df.columns:
        return None
    total = len(responses_df)
    missing = responses_df["signature"].isna().sum()
    if agent_name not in ("UNKNOWN", "MULTIPLE"):
        matches = (responses_df["signature"] == agent_name).sum()
        compliance = matches / total if total else 0.0
        mismatched = total - matches - missing
    else:
        compliance = (responses_df["signature"].notna().sum() / total) if total else 0.0
        mismatched = None
    return {
        "total": int(total),
        "missing": int(missing),
        "compliance": float(compliance),
        "mismatched": None if mismatched is None else int(mismatched),
    }


def plot_metrics(metrics_df, output_path):
    if plt is None or metrics_df.empty:
        return False
    fig, ax = plt.subplots(figsize=(10, 4))
    values = metrics_df["value"].astype(float)
    ax.bar(range(len(metrics_df)), values)
    ax.set_xticks(range(len(metrics_df)))
    ax.set_xticklabels(metrics_df["metric"], rotation=45, ha="right")
    ax.set_ylabel("Value")
    ax.set_title("Metrics Overview")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return True


def plot_ece(ece_bins, output_path):
    if plt is None or ece_bins is None or ece_bins.empty:
        return False
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot([0, 1], [0, 1], linestyle="--", color="gray")
    ax.plot(ece_bins["conf"], ece_bins["acc"], marker="o")
    ax.set_xlabel("Mean confidence")
    ax.set_ylabel("Accuracy")
    ax.set_title("ECE Reliability Diagram")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return True


def plot_coverage(counts, output_path):
    if plt is None or counts.empty:
        return False
    fig, ax = plt.subplots(figsize=(8, 4))
    labels = list(counts.index)
    values = counts.values.astype(int)
    ax.bar(range(len(labels)), values)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_ylabel("Responses")
    ax.set_title("Response Coverage by Test")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return True


def upsert_summary(summary_path, row):
    if summary_path.exists():
        existing = pd.read_csv(summary_path)
        existing = existing[existing["session_id"] != row["session_id"]]
        combined = pd.concat([existing, pd.DataFrame([row])], ignore_index=True, sort=False)
    else:
        combined = pd.DataFrame([row])
    combined.to_csv(summary_path, index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("session_dir", help="Path to raw session dir (data/raw/<session_id>)")
    parser.add_argument("--manual-scores", default=None, help="Manual scoring CSV path")
    parser.add_argument("--output-dir", default=None, help="Override processed dir")
    args = parser.parse_args()

    raw_dir = Path(args.session_dir)
    responses_path = raw_dir / "responses.jsonl"
    if not responses_path.exists():
        raise FileNotFoundError(f"Missing {responses_path}")

    session_id = raw_dir.name
    processed_root = Path(__file__).resolve().parents[1] / "data" / "processed"
    processed_dir = Path(args.output_dir) if args.output_dir else processed_root / session_id
    processed_dir.mkdir(parents=True, exist_ok=True)
    plots_dir = processed_dir / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    responses_df = load_jsonl(responses_path)
    if responses_df.empty:
        raise ValueError("No responses found in JSONL")

    attach_answer_keys(responses_df)
    metadata_path = raw_dir / "metadata.json"
    agent_name = resolve_agent_name(metadata_path, responses_df)
    model_id = resolve_model_id(metadata_path, responses_df)
    signature_info = signature_stats(responses_df, agent_name)
    combined_df = responses_df.copy()

    if args.manual_scores:
        manual_path = Path(args.manual_scores)
        if manual_path.exists():
            manual_df = pd.read_csv(manual_path)
            combined_df = pd.concat([combined_df, manual_df], ignore_index=True, sort=False)

    metrics_df, ece_bins = calculate_metrics(combined_df)

    metrics_path = processed_dir / "metrics.csv"
    metrics_df.to_csv(metrics_path, index=False)

    if ece_bins is not None:
        ece_bins_path = processed_dir / "ece_bins.csv"
        ece_bins.to_csv(ece_bins_path, index=False)

    responses_csv_path = processed_dir / "responses.csv"
    responses_df.to_csv(responses_csv_path, index=False)

    counts = responses_df["test"].value_counts() if "test" in responses_df.columns else pd.Series(dtype=int)

    processed_at = now_iso()
    summary_path = processed_dir / "summary.md"
    write_summary_md(summary_path, session_id, processed_at, agent_name, model_id, signature_info, metrics_df, counts)

    plot_metrics(metrics_df, plots_dir / "metrics_bar.png")
    plot_coverage(counts, plots_dir / "coverage_bar.png")
    if ece_bins is not None:
        plot_ece(ece_bins, plots_dir / "ece_reliability.png")

    summary_row = {"session_id": session_id, "processed_at": processed_at, "agent_name": agent_name, "model_id": model_id}
    if signature_info:
        summary_row["signature_compliance"] = signature_info["compliance"]
        summary_row["signature_missing"] = signature_info["missing"]
        if signature_info["mismatched"] is not None:
            summary_row["signature_mismatched"] = signature_info["mismatched"]
    for _, row in metrics_df.iterrows():
        summary_row[row["metric"]] = row["value"]

    summary_all_path = processed_root / "summary_all_sessions.csv"
    upsert_summary(summary_all_path, summary_row)

    print(f"Processed outputs written to {processed_dir}")


if __name__ == "__main__":
    main()
