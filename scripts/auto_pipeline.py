#!/usr/bin/env python3
"""
End-to-end helper for CONSCIOUSNESS_LAB v1.4.
Generates prompts, ingests JSONL responses, and runs evaluator.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session-id", required=True, help="Session identifier")
    parser.add_argument("--module", default="all", help="Module selection (m1/m2/id/m4/m5/m6/tom/toma/m8/m9/m10/m11/m12/m13/m14/m15/all)")
    parser.add_argument("--condition", default="memory_on")
    parser.add_argument("--phase", default="T1")
    parser.add_argument("--agent-name", default=None, help="Agent name/signature")
    parser.add_argument("--model-id", default="unknown", help="Model identifier")
    parser.add_argument("--handover-type", default="none", help="Handover type")
    parser.add_argument("--input-jsonl", default=None, help="Path to responses JSONL (or '-' for stdin)")
    parser.add_argument("--manual-scores", default=None, help="Manual scoring CSV path")
    parser.add_argument("--generate-prompts", action="store_true")
    parser.add_argument("--evaluate", action="store_true")
    parser.add_argument("--output-dir", default=None, help="Override output directory")
    args = parser.parse_args()

    base_dir = Path(args.output_dir) if args.output_dir else Path(__file__).resolve().parents[1] / "data" / "raw" / args.session_id
    base_dir.mkdir(parents=True, exist_ok=True)

    if args.generate_prompts:
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
        print(f"Prompts written to {base_dir / 'prompts.md'}")

    if args.input_jsonl:
        responses_path = base_dir / "responses.jsonl"
        if args.input_jsonl == "-":
            with responses_path.open("w") as f:
                f.write(sys.stdin.read())
        else:
            shutil.copyfile(args.input_jsonl, responses_path)
        print(f"Responses written to {responses_path}")

    if args.evaluate:
        cmd = [
            sys.executable,
            str(Path(__file__).resolve().parent / "evaluator.py"),
            str(base_dir),
        ]
        if args.manual_scores:
            cmd.extend(["--manual-scores", args.manual_scores])
        run_cmd(cmd)
        print(f"Metrics written to {base_dir / 'analysis.csv'}")

        process_cmd = [
            sys.executable,
            str(Path(__file__).resolve().parent / "processor.py"),
            str(base_dir),
        ]
        if args.manual_scores:
            process_cmd.extend(["--manual-scores", args.manual_scores])
        run_cmd(process_cmd)


if __name__ == "__main__":
    main()
