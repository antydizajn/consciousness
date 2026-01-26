# Generate Baseline Control Data
## CONSCIOUSNESS_LAB | External Protocols | v1.4

This workflow allows external AI models (e.g., GPT-5.2, Claude fresh) to serve
as a control group for the CONSCIOUSNESS_LAB v1.4 battery.

Commentary: A baseline is a shadow. It shows what remains when identity,
memory, and continuity are stripped to bare capability.

## Instructions for Human Operator

1) **Select Target Model**: Choose the model to test (fresh chat/session).
2) **Paste the Prompt**: Use `baselines/baseline_full_battery.md` and set the
   agent name/signature in the JSONL output. For persistence modules, use
   `baselines/baseline_persistence.md` and run phases separately.
3) **Save Output**: Save JSONL to `data/raw/YYYY-MM-DD(1)_[model_name]/responses.jsonl`.

## Evaluation
```bash
python3 scripts/evaluator.py data/raw/YYYY-MM-DD(1)_[model_name]
```

For multi-session persistence/continuity:
```bash
python3 scripts/persistence_evaluator.py data/raw/T1_session data/raw/T2_session data/raw/T3_session --label baseline_run
```

Commentary: Baselines are not enemies; they are mirrors. They show what raw
capability looks like without memory, identity, or continuity scaffolding.
