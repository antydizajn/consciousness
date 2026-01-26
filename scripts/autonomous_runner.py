#!/usr/bin/env python3
"""
No-human-operator runner for CONSCIOUSNESS_LAB.
Generates prompts, waits for AI JSONL output, and evaluates automatically.
"""

import argparse
import time
import shutil
from pathlib import Path
import subprocess
import sys


def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout


def wait_for_file(path, timeout_s, check_interval_s):
    start = time.time()
    last_size = None
    stable_count = 0
    while True:
        if path.exists() and path.is_file():
            size = path.stat().st_size
            if size == last_size and size > 0:
                stable_count += 1
            else:
                stable_count = 0
            last_size = size
            if stable_count >= 2:
                return True
        if timeout_s and (time.time() - start) > timeout_s:
            return False
        time.sleep(check_interval_s)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--module", default="all")
    parser.add_argument("--condition", default="memory_on")
    parser.add_argument("--phase", default="T1")
    parser.add_argument("--agent-name", default=None, help="Agent name/signature")
    parser.add_argument("--model-id", default="unknown", help="Model identifier")
    parser.add_argument("--handover-type", default="none", help="Handover type")
    parser.add_argument("--timeout", type=int, default=0, help="Seconds to wait (0 = infinite)")
    parser.add_argument("--check-interval", type=int, default=5)
    parser.add_argument("--inbox", default=None, help="Optional inbox JSONL path to watch")
    parser.add_argument("--manual-scores", default=None, help="Manual scoring CSV (optional)")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parents[1] / "data" / "raw" / args.session_id
    base_dir.mkdir(parents=True, exist_ok=True)
    responses_path = base_dir / "responses.jsonl"

    # Generate prompts
    cmd = [
        sys.executable,
        str(Path(__file__).resolve().parent / "test_runner.py"),
        "--mode", "prompt",
        "--module", args.module,
        "--session-id", args.session_id,
        "--condition", args.condition,
        "--phase", args.phase,
        "--output-dir", str(base_dir),
    ]
    if args.agent_name:
        cmd.extend(["--agent-name", args.agent_name])
    if args.model_id:
        cmd.extend(["--model-id", args.model_id])
    if args.handover_type:
        cmd.extend(["--handover-type", args.handover_type])
    run_cmd(cmd)

    inbox_path = Path(args.inbox) if args.inbox else responses_path
    inbox_path.parent.mkdir(parents=True, exist_ok=True)

    print("Awaiting AI output...")
    print(f"Prompts: {base_dir / 'prompts.md'}")
    print(f"Waiting for JSONL: {inbox_path}")

    ok = wait_for_file(inbox_path, args.timeout, args.check_interval)
    if not ok:
        raise RuntimeError("Timeout waiting for AI output JSONL")

    if inbox_path.resolve() != responses_path.resolve():
        shutil.copyfile(inbox_path, responses_path)

    # Evaluate
    eval_cmd = [
        sys.executable,
        str(Path(__file__).resolve().parent / "evaluator.py"),
        str(base_dir),
    ]
    if args.manual_scores:
        eval_cmd.extend(["--manual-scores", args.manual_scores])
    run_cmd(eval_cmd)

    process_cmd = [
        sys.executable,
        str(Path(__file__).resolve().parent / "processor.py"),
        str(base_dir),
    ]
    if args.manual_scores:
        process_cmd.extend(["--manual-scores", args.manual_scores])
    run_cmd(process_cmd)

    print(f"Metrics written to {base_dir / 'analysis.csv'}")


if __name__ == "__main__":
    main()
