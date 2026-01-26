#!/usr/bin/env python3
"""
Compare responses across two sessions for a given test and key field.
"""

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

import pandas as pd


TOKEN_RE = re.compile(r"[a-z0-9]+")


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
    return pd.DataFrame(records)


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("left", help="Left session dir")
    parser.add_argument("right", help="Right session dir")
    parser.add_argument("--test", default=None, help="Filter by test name (e.g., M12)")
    parser.add_argument("--key", default=None, help="Key field (pair_id or item_id)")
    parser.add_argument("--phase-left", default=None, help="Phase filter for left session")
    parser.add_argument("--phase-right", default=None, help="Phase filter for right session")
    parser.add_argument("--output", default=None, help="Output CSV path")
    args = parser.parse_args()

    left_df = load_session(args.left)
    right_df = load_session(args.right)

    if args.test:
        left_df = left_df[left_df.get("test") == args.test]
        right_df = right_df[right_df.get("test") == args.test]

    if args.phase_left:
        left_df = left_df[left_df.get("phase") == args.phase_left]
    if args.phase_right:
        right_df = right_df[right_df.get("phase") == args.phase_right]

    key_field = args.key
    if not key_field:
        key_field = "pair_id" if "pair_id" in left_df.columns and "pair_id" in right_df.columns else "item_id"

    left_df = left_df[left_df[key_field].notna()]
    right_df = right_df[right_df[key_field].notna()]

    left_map = dict(zip(left_df[key_field], left_df.get("response")))
    right_map = dict(zip(right_df[key_field], right_df.get("response")))

    keys = sorted(set(left_map.keys()) & set(right_map.keys()))
    rows = []
    for key in keys:
        sim = cosine_similarity(left_map[key], right_map[key])
        rows.append({"key": key, "similarity": sim})

    out_path = Path(args.output) if args.output else Path("session_comparison.csv")
    pd.DataFrame(rows).to_csv(out_path, index=False)
    print(f"Wrote comparison to {out_path}")


if __name__ == "__main__":
    main()
