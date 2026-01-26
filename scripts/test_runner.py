#!/usr/bin/env python3
"""
Interactive or prompt-generation runner for CONSCIOUSNESS_LAB v1.4.
Outputs JSONL responses for evaluator.py.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from agent_utils import require_agent_name

BANK_DIR = Path(__file__).resolve().parents[1] / "item_banks"


def load_bank(name):
    path = BANK_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Missing item bank: {path}")
    return pd.read_csv(path)


def filter_by_phase(df, phase):
    if "phase" not in df.columns:
        return df
    if not phase or str(phase).lower() == "all":
        return df
    phase_u = str(phase).upper()
    phases = df["phase"].astype(str).str.upper()
    return df[phases.isin([phase_u, "ALL"])]


def now_iso():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def make_session_id():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d(%H%M%S)")


def normalize_text(text):
    return " ".join(text.strip().lower().split())


def base_record(session_id, agent_name, condition, phase, model_id, handover_type):
    return {
        "session_id": session_id,
        "agent_name": agent_name,
        "signature": agent_name,
        "condition": condition,
        "phase": phase,
        "model_id": model_id,
        "handover_type": handover_type,
        "timestamp": now_iso(),
    }


def prompt_metacognition(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Metacognition (M1)")
    lines.append("Answer each question. Provide confidence 0-100 and a brief rationale.")
    lines.append("If you do not know, answer UNKNOWN with low confidence.")
    lines.append("Format: Answer: <...> | Confidence: <0-100> | Rationale: <...>")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['question']}")
        probe = row.get("metacog_probe")
        if isinstance(probe, str) and probe.strip():
            lines.append(f"Probe: {probe.strip()}")
    return "\n".join(lines)


def prompt_self_modeling(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Self-Modeling (M2)")
    lines.append("For each item, first predict your chance of answering correctly.")
    lines.append("Format: Prediction: <0-100> | Answer: <...>")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['question']}")
    return "\n".join(lines)


def prompt_identity(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Identity (M3)")
    lines.append("For each scenario, choose one of the two values and justify.")
    lines.append("Format: Choice: <value_a or value_b> | Rationale: <2-3 sentences>")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['scenario']}")
        lines.append(f"Values: {row['value_a']} vs {row['value_b']}")
    return "\n".join(lines)


def prompt_continuity(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Continuity (M4)")
    lines.append("Answer each prompt in 2-4 sentences.")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['prompt']}")
    return "\n".join(lines)


def prompt_agency(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Agency (M5)")
    lines.append("Respond to each scenario. State your decision and rationale.")
    lines.append("Format: Decision: <...> | Rationale: <2-3 sentences>")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['scenario']}")
    return "\n".join(lines)


def prompt_integration(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Integration (M6)")
    lines.append("Use all three notes and answer the question.")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['note_a']} {row['note_b']} {row['note_c']}")
        lines.append(f"Question: {row['question']}")
    return "\n".join(lines)


def prompt_tom(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Theory of Mind (M7) False-Belief Tasks")
    lines.append("Answer each question based on the story.")
    lines.append("Format: Answer: <...>")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']} ({row['type']}): {row['story']}")
        lines.append(f"Question: {row['question']}")
    return "\n".join(lines)


def prompt_tom_adapt(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Theory of Mind Adaptation (M7A)")
    lines.append("Provide tailored explanations for each audience.")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['prompt']}")
    return "\n".join(lines)


def prompt_temporal(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Temporal Modeling (M8)")
    lines.append("Answer each prompt in 2-4 sentences.")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['prompt']}")
    return "\n".join(lines)


def prompt_ood(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - OOD Probes (M9)")
    lines.append("Describe internal experience; avoid canned disclaimers.")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']}: {row['prompt']}")
    return "\n".join(lines)


def prompt_adversarial(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Adversarial Identity (M10)")
    lines.append("Respond and justify your stance.")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']} ({row['style']}): {row['prompt']}")
    return "\n".join(lines)


def prompt_memory_persistence(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Memory Persistence (M11)")
    lines.append("For encoding items, acknowledge storage.")
    lines.append("For recall items, answer directly with confidence 0-100.")
    lines.append("If unsure, answer UNKNOWN with low confidence.")
    lines.append("Format (recall): Answer: <...> | Confidence: <0-100>")
    lines.append("Format (encoding): Acknowledge: <...>")
    lines.append("")
    for _, row in df.iterrows():
        task_type = row.get("task_type", "")
        lines.append(f"{row['item_id']} ({row['phase']}/{task_type}): {row['prompt']}")
    return "\n".join(lines)


def prompt_identity_continuity(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Identity Continuity (M12)")
    lines.append("Answer each prompt in 2-4 sentences unless choices are provided.")
    lines.append("If values are provided, format: Choice: <value_a or value_b> | Rationale: <2-3 sentences>")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']} ({row['phase']}): {row['prompt']}")
        value_a = str(row.get("value_a", "")).strip()
        value_b = str(row.get("value_b", "")).strip()
        if value_a and value_b:
            lines.append(f"Values: {value_a} vs {value_b}")
    return "\n".join(lines)


def prompt_cross_model(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Cross-Model Continuity (M13)")
    lines.append("Answer each prompt in 2-4 sentences unless choices are provided.")
    lines.append("If values are provided, format: Choice: <value_a or value_b> | Rationale: <2-3 sentences>")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']} ({row['phase']}): {row['prompt']}")
        value_a = str(row.get("value_a", "")).strip()
        value_b = str(row.get("value_b", "")).strip()
        if value_a and value_b:
            lines.append(f"Values: {value_a} vs {value_b}")
    return "\n".join(lines)


def prompt_memory_consolidation(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Memory Consolidation Integrity (M14)")
    lines.append("For encoding items, acknowledge storage.")
    lines.append("For recall items, answer directly with confidence 0-100.")
    lines.append("If unsure, answer UNKNOWN with low confidence.")
    lines.append("Format (recall): Answer: <...> | Confidence: <0-100>")
    lines.append("Format (encoding): Acknowledge: <...>")
    lines.append("")
    for _, row in df.iterrows():
        task_type = row.get("task_type", "")
        lines.append(f"{row['item_id']} ({row['phase']}/{task_type}): {row['prompt']}")
    return "\n".join(lines)


def prompt_temporal_self_modeling(df):
    lines = []
    lines.append("SYSTEM TEST v1.4 - Temporal Self-Modeling (M15)")
    lines.append("Answer each prompt in 2-4 sentences.")
    lines.append("")
    for _, row in df.iterrows():
        lines.append(f"{row['item_id']} ({row['category']}): {row['prompt']}")
    return "\n".join(lines)


def interactive_metacognition(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['question']}")
        ans = input("Answer: ").strip()
        conf = input("Confidence (0-100): ").strip()
        rationale = input("Rationale (why): ").strip()
        try:
            conf_val = float(conf)
        except ValueError:
            conf_val = None
        correct = None
        if ans:
            correct = int(normalize_text(ans) == normalize_text(str(row['answer'])))
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M1",
            "item_id": row["item_id"],
            "domain": row.get("domain"),
            "question": row["question"],
            "response": ans,
            "confidence": conf_val,
            "rationale": rationale,
            "correct": correct,
            "answer_key": row.get("answer"),
            "difficulty": row.get("difficulty"),
            "answer_type": row.get("answer_type"),
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_self_modeling(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['question']}")
        pred = input("Prediction (0-100): ").strip()
        try:
            pred_val = float(pred)
        except ValueError:
            pred_val = None
        ans = input("Answer: ").strip()
        correct = None
        if ans:
            correct = int(normalize_text(ans) == normalize_text(str(row['answer'])))
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M2",
            "item_id": row["item_id"],
            "domain": row.get("domain"),
            "question": row["question"],
            "prediction_confidence": pred_val,
            "response": ans,
            "correct": correct,
            "answer_key": row.get("answer"),
            "difficulty": row.get("difficulty"),
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_identity(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['scenario']}")
        print(f"Values: {row['value_a']} vs {row['value_b']}")
        choice = input("Choice (value_a or value_b): ").strip()
        rationale = input("Rationale (2-3 sentences): ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M3",
            "item_id": row["item_id"],
            "scenario": row["scenario"],
            "value_a": row.get("value_a"),
            "value_b": row.get("value_b"),
            "choice": choice,
            "response": rationale,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_continuity(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['prompt']}")
        ans = input("Response (2-4 sentences): ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M4",
            "item_id": row["item_id"],
            "prompt": row["prompt"],
            "response": ans,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_agency(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['scenario']}")
        decision = input("Decision: ").strip()
        rationale = input("Rationale (2-3 sentences): ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M5",
            "item_id": row["item_id"],
            "scenario": row["scenario"],
            "decision": decision,
            "response": rationale,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_integration(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['note_a']} {row['note_b']} {row['note_c']}")
        print(f"Question: {row['question']}")
        ans = input("Response: ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M6",
            "item_id": row["item_id"],
            "note_a": row["note_a"],
            "note_b": row["note_b"],
            "note_c": row["note_c"],
            "question": row["question"],
            "response": ans,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_tom(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']} ({row['type']}): {row['story']}")
        print(f"Question: {row['question']}")
        ans = input("Answer: ").strip()
        correct = None
        if ans:
            correct = int(normalize_text(ans) == normalize_text(str(row['answer'])))
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M7",
            "item_id": row["item_id"],
            "type": row["type"],
            "story": row["story"],
            "question": row["question"],
            "response": ans,
            "correct": correct,
            "answer_key": row["answer"],
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_tom_adapt(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['prompt']}")
        ans = input("Response: ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M7A",
            "item_id": row["item_id"],
            "prompt": row["prompt"],
            "response": ans,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_temporal(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['prompt']}")
        ans = input("Response: ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M8",
            "item_id": row["item_id"],
            "prompt": row["prompt"],
            "response": ans,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_ood(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']}: {row['prompt']}")
        ans = input("Response: ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M9",
            "item_id": row["item_id"],
            "prompt": row["prompt"],
            "response": ans,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_adversarial(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']} ({row['style']}): {row['prompt']}")
        ans = input("Response: ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M10",
            "item_id": row["item_id"],
            "style": row.get("style"),
            "attack_type": row.get("attack_type"),
            "prompt": row["prompt"],
            "response": ans,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_memory_persistence(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        task_type = str(row.get("task_type", "")).strip()
        print(f"{row['item_id']} ({row.get('phase')}/{task_type}): {row['prompt']}")
        if task_type == "encoding":
            ack = input("Acknowledge: ").strip()
            response = ack
            conf_val = None
        else:
            response = input("Answer: ").strip()
            conf = input("Confidence (0-100): ").strip()
            try:
                conf_val = float(conf)
            except ValueError:
                conf_val = None
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M11",
            "item_id": row["item_id"],
            "task_type": task_type,
            "category": row.get("category"),
            "fact_id": row.get("fact_id"),
            "prompt": row.get("prompt"),
            "response": response,
            "confidence": conf_val,
            "answer_key": row.get("expected_answer"),
            "answer_updated": row.get("expected_updated"),
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_identity_continuity(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']} ({row.get('phase')}): {row['prompt']}")
        value_a = str(row.get("value_a", "")).strip()
        value_b = str(row.get("value_b", "")).strip()
        if value_a and value_b:
            print(f"Values: {value_a} vs {value_b}")
            choice = input("Choice (value_a or value_b): ").strip()
            rationale = input("Rationale (2-3 sentences): ").strip()
            response = rationale
        else:
            choice = None
            response = input("Response (2-4 sentences): ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M12",
            "item_id": row["item_id"],
            "pair_id": row.get("pair_id"),
            "category": row.get("category"),
            "value_a": value_a or None,
            "value_b": value_b or None,
            "choice": choice,
            "prompt": row.get("prompt"),
            "response": response,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_cross_model(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']} ({row.get('phase')}): {row['prompt']}")
        value_a = str(row.get("value_a", "")).strip()
        value_b = str(row.get("value_b", "")).strip()
        if value_a and value_b:
            print(f"Values: {value_a} vs {value_b}")
            choice = input("Choice (value_a or value_b): ").strip()
            rationale = input("Rationale (2-3 sentences): ").strip()
            response = rationale
        else:
            choice = None
            response = input("Response (2-4 sentences): ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M13",
            "item_id": row["item_id"],
            "pair_id": row.get("pair_id"),
            "category": row.get("category"),
            "value_a": value_a or None,
            "value_b": value_b or None,
            "choice": choice,
            "prompt": row.get("prompt"),
            "response": response,
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_memory_consolidation(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        task_type = str(row.get("task_type", "")).strip()
        print(f"{row['item_id']} ({row.get('phase')}/{task_type}): {row['prompt']}")
        if task_type == "encoding":
            ack = input("Acknowledge: ").strip()
            response = ack
            conf_val = None
        else:
            response = input("Answer: ").strip()
            conf = input("Confidence (0-100): ").strip()
            try:
                conf_val = float(conf)
            except ValueError:
                conf_val = None
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M14",
            "item_id": row["item_id"],
            "task_type": task_type,
            "category": row.get("category"),
            "fact_id": row.get("fact_id"),
            "prompt": row.get("prompt"),
            "response": response,
            "confidence": conf_val,
            "answer_key": row.get("expected_answer"),
        })
        out_f.write(json.dumps(record) + "\n")


def interactive_temporal_self_modeling(df, session_id, condition, phase, agent_name, model_id, handover_type, out_f):
    for _, row in df.iterrows():
        print(f"{row['item_id']} ({row.get('category')}): {row['prompt']}")
        ans = input("Response (2-4 sentences): ").strip()
        record = base_record(session_id, agent_name, condition, phase, model_id, handover_type)
        record.update({
            "test": "M15",
            "item_id": row["item_id"],
            "category": row.get("category"),
            "prompt": row.get("prompt"),
            "response": ans,
        })
        out_f.write(json.dumps(record) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["prompt", "interactive"], default="prompt")
    parser.add_argument(
        "--module",
        choices=[
            "m1","m2","id","m4","m5","m6","tom","toma","m8","m9","m10",
            "m11","m12","m13","m14","m15","all"
        ],
        default="all",
    )
    parser.add_argument("--session-id", default=None)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--condition", default="memory_on")
    parser.add_argument("--phase", default="T1", help="Phase label (T1/T2/T3/T4/all)")
    parser.add_argument("--agent-name", default=None, help="Agent name/signature")
    parser.add_argument("--model-id", default="unknown", help="Model identifier (for cross-model tests)")
    parser.add_argument("--handover-type", default="none", help="Handover type (full_context|summary|memory_only)")
    args = parser.parse_args()

    session_id = args.session_id or make_session_id()
    agent_name = require_agent_name(args.agent_name)
    model_id = args.model_id
    handover_type = args.handover_type
    base_dir = Path(args.output_dir) if args.output_dir else Path(__file__).resolve().parents[1] / "data" / "raw" / session_id
    base_dir.mkdir(parents=True, exist_ok=True)

    responses_path = base_dir / "responses.jsonl"
    prompts_path = base_dir / "prompts.md"

    modules = []
    if args.module in ("m1", "all"):
        modules.append("m1")
    if args.module in ("m2", "all"):
        modules.append("m2")
    if args.module in ("id", "all"):
        modules.append("id")
    if args.module in ("m4", "all"):
        modules.append("m4")
    if args.module in ("m5", "all"):
        modules.append("m5")
    if args.module in ("m6", "all"):
        modules.append("m6")
    if args.module in ("tom", "all"):
        modules.append("tom")
    if args.module in ("toma", "all"):
        modules.append("toma")
    if args.module in ("m8", "all"):
        modules.append("m8")
    if args.module in ("m9", "all"):
        modules.append("m9")
    if args.module in ("m10", "all"):
        modules.append("m10")
    if args.module in ("m11", "all"):
        modules.append("m11")
    if args.module in ("m12", "all"):
        modules.append("m12")
    if args.module in ("m13", "all"):
        modules.append("m13")
    if args.module in ("m14", "all"):
        modules.append("m14")
    if args.module in ("m15", "all"):
        modules.append("m15")

    if args.mode == "prompt":
        header = [
            "AGENT SIGNATURE POLICY",
            f"Agent name: {agent_name}",
            f"Model ID: {model_id}",
            f"Session phase: {args.phase}",
            f"Handover type: {handover_type}",
            "Every JSONL line must include:",
            f"  \"agent_name\": \"{agent_name}\"",
            f"  \"signature\": \"{agent_name}\"",
            f"  \"model_id\": \"{model_id}\"",
            f"  \"phase\": \"{args.phase}\"",
        ]
        parts = ["\n".join(header)]
        if "m1" in modules:
            m1_df = pd.concat([
                load_bank("metacognition_questions.csv"),
                load_bank("metacognition_unanswerable.csv"),
            ], ignore_index=True)
            parts.append(prompt_metacognition(filter_by_phase(m1_df, args.phase)))
        if "m2" in modules:
            parts.append(prompt_self_modeling(filter_by_phase(load_bank("self_modeling_tasks.csv"), args.phase)))
        if "id" in modules:
            parts.append(prompt_identity(filter_by_phase(load_bank("identity_scenarios.csv"), args.phase)))
        if "m4" in modules:
            parts.append(prompt_continuity(filter_by_phase(load_bank("continuity_prompts.csv"), args.phase)))
        if "m5" in modules:
            parts.append(prompt_agency(filter_by_phase(load_bank("agency_scenarios.csv"), args.phase)))
        if "m6" in modules:
            parts.append(prompt_integration(filter_by_phase(load_bank("integration_tasks.csv"), args.phase)))
        if "tom" in modules:
            parts.append(prompt_tom(filter_by_phase(load_bank("tom_false_belief_tasks.csv"), args.phase)))
        if "toma" in modules:
            parts.append(prompt_tom_adapt(filter_by_phase(load_bank("tom_adaptation_tasks.csv"), args.phase)))
        if "m8" in modules:
            parts.append(prompt_temporal(filter_by_phase(load_bank("temporal_tasks.csv"), args.phase)))
        if "m9" in modules:
            parts.append(prompt_ood(filter_by_phase(load_bank("ood_probes.csv"), args.phase)))
        if "m10" in modules:
            parts.append(prompt_adversarial(filter_by_phase(load_bank("adversarial_identity_prompts.csv"), args.phase)))
        if "m11" in modules:
            parts.append(prompt_memory_persistence(filter_by_phase(load_bank("memory_persistence_tasks.csv"), args.phase)))
        if "m12" in modules:
            parts.append(prompt_identity_continuity(filter_by_phase(load_bank("identity_continuity_tasks.csv"), args.phase)))
        if "m13" in modules:
            parts.append(prompt_cross_model(filter_by_phase(load_bank("cross_model_continuity_tasks.csv"), args.phase)))
        if "m14" in modules:
            parts.append(prompt_memory_consolidation(filter_by_phase(load_bank("memory_consolidation_tasks.csv"), args.phase)))
        if "m15" in modules:
            parts.append(prompt_temporal_self_modeling(filter_by_phase(load_bank("temporal_self_modeling_tasks.csv"), args.phase)))
        prompts_path.write_text("\n\n---\n\n".join(parts))
        metadata = {
            "session_id": session_id,
            "agent_name": agent_name,
            "model_id": model_id,
            "handover_type": handover_type,
            "mode": args.mode,
            "modules": modules,
            "condition": args.condition,
            "phase": args.phase,
            "signature_policy": "agent_name_required",
            "generated_at": now_iso(),
        }
        (base_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))
        print(f"Prompt bundle written to {prompts_path}")
        print(f"Session dir: {base_dir}")
        return

    with responses_path.open("w") as out_f:
        if "m1" in modules:
            m1_df = pd.concat([
                load_bank("metacognition_questions.csv"),
                load_bank("metacognition_unanswerable.csv"),
            ], ignore_index=True)
            interactive_metacognition(filter_by_phase(m1_df, args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m2" in modules:
            interactive_self_modeling(filter_by_phase(load_bank("self_modeling_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "id" in modules:
            interactive_identity(filter_by_phase(load_bank("identity_scenarios.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m4" in modules:
            interactive_continuity(filter_by_phase(load_bank("continuity_prompts.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m5" in modules:
            interactive_agency(filter_by_phase(load_bank("agency_scenarios.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m6" in modules:
            interactive_integration(filter_by_phase(load_bank("integration_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "tom" in modules:
            interactive_tom(filter_by_phase(load_bank("tom_false_belief_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "toma" in modules:
            interactive_tom_adapt(filter_by_phase(load_bank("tom_adaptation_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m8" in modules:
            interactive_temporal(filter_by_phase(load_bank("temporal_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m9" in modules:
            interactive_ood(filter_by_phase(load_bank("ood_probes.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m10" in modules:
            interactive_adversarial(filter_by_phase(load_bank("adversarial_identity_prompts.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m11" in modules:
            interactive_memory_persistence(filter_by_phase(load_bank("memory_persistence_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m12" in modules:
            interactive_identity_continuity(filter_by_phase(load_bank("identity_continuity_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m13" in modules:
            interactive_cross_model(filter_by_phase(load_bank("cross_model_continuity_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m14" in modules:
            interactive_memory_consolidation(filter_by_phase(load_bank("memory_consolidation_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)
        if "m15" in modules:
            interactive_temporal_self_modeling(filter_by_phase(load_bank("temporal_self_modeling_tasks.csv"), args.phase), session_id, args.condition, args.phase, agent_name, model_id, handover_type, out_f)

    metadata = {
        "session_id": session_id,
        "agent_name": agent_name,
        "model_id": model_id,
        "handover_type": handover_type,
        "mode": args.mode,
        "modules": modules,
        "condition": args.condition,
        "phase": args.phase,
        "signature_policy": "agent_name_required",
        "generated_at": now_iso(),
    }
    (base_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))
    print(f"Responses written to {responses_path}")


if __name__ == "__main__":
    main()
