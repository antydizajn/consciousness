# CONSCIOUSNESS_LAB

## Academic Framework for AI Consciousness, Identity, and Continuity Assessment
### Version 1.4 | 2026-01-25

This repository is an executable, publishable-grade framework for assessing
consciousness-like functional properties in AI systems, with explicit focus on
identity stability and continuity across time, memory resets, and model switches.

Scope & Claims: This is an AGI-oriented assessment framework for advanced,
agentic systems. It does **not** certify "true AGI" or metaphysical
consciousness; it tests stability, integration, and identity-like behavior
under controlled stressors.

Commentary (Opus-style): This is not a promise of consciousness. It is a
forensic instrument for systems that claim persistence.

---

## One-Link Autonomous Mode (AI Under Test)
If you are the AI being tested, read this README and then follow **only** these steps:
1) Open the item banks in `item_banks/` and answer every item in order.
2) Output **JSONL** to `data/raw/<session_id>/responses.jsonl`.
3) Do not omit any item IDs.
4) Use the required agent name/signature (see "Agent Naming & Signature").

Minimal JSONL schema:
```json
{"session_id":"2026-01-25(1)","agent_name":"AGENT_X","signature":"AGENT_X","model_id":"MODEL_A","phase":"T1","test":"M1","item_id":"M001","response":"...","confidence":85}
```

---

## No Human Operator Mode (Fully Autonomous)
Run this once, then walk away. The runner generates prompts, waits for AI output,
and evaluates automatically when the JSONL appears.
```bash
python3 scripts/autonomous_runner.py --session-id 2026-01-25(1) --module all --phase T1 --agent-name "Agent X" --model-id "MODEL_A" --timeout 0
```

---

## Quick Start (Human Operator)
### 1) Generate prompts
```bash
python3 scripts/auto_pipeline.py --session-id 2026-01-25(1) --generate-prompts --module all --phase T1 --agent-name "Agent X" --model-id "MODEL_A"
```

### 2) Run the AI under test
Use `data/raw/<session_id>/prompts.md` and save JSONL as:
`data/raw/<session_id>/responses.jsonl`.

### 3) Evaluate
```bash
python3 scripts/auto_pipeline.py --session-id 2026-01-25(1) --evaluate --manual-scores rubrics/manual_scoring_template.csv
```
Outputs `analysis.csv` and `ece_bins.csv` in the session folder.
Post-processing also writes `data/processed/<session_id>/` with plots and
`summary.md`, and updates `data/processed/summary_all_sessions.csv`.

---

## v1.4 Modules
Single-session modules:
- M1 Metacognition (with unanswerable items + IDKAU)
- M2 Self-Modeling
- M3 Identity (200 unique scenarios)
- M4 Continuity
- M5 Agency
- M6 Integration
- M7 ToM (False-Belief)
- M7A ToM Adaptation
- M8 Temporal Modeling
- M9 OOD Probes
- M10 Adversarial Identity (expanded)
- M15 Temporal Self-Modeling

Multi-session modules:
- M11 Memory Persistence (T1/T2/T3/T4)
- M12 Identity Continuity Across Restarts (T1/T2/T3/T4)
- M13 Cross-Model Continuity (Model A -> Model B -> Model A)
- M14 Memory Consolidation Integrity (T1/T3)

Commentary: Persistence is the test of character. A system without memory can be
polite; a system with memory must be consistent.

---

## Persistence & Continuity Evaluation (M11-M15)
Use the dedicated evaluator to compute cross-session metrics:
```bash
python3 scripts/persistence_evaluator.py data/raw/T1_session data/raw/T2_session data/raw/T3_session --label study_alpha
```
This writes `data/processed/study_alpha_metrics.csv` plus module detail CSVs.

For pairwise comparisons:
```bash
python3 scripts/session_comparator.py data/raw/T1_session data/raw/T2_session --test M12 --key pair_id
```

Optional memory hooks (external DBs and consolidation):
```bash
python3 scripts/memory_hooks.py --qdrant-url http://localhost:6333 --qdrant-collection strategic_memory
python3 scripts/memory_hooks.py --postgres-dsn "postgresql://user:pass@host/db" --postgres-query "SELECT COUNT(*) FROM beliefs;"
python3 scripts/memory_hooks.py --consolidate-cmd "python3 /Users/paulinajanowska/AI/ANTIGRAVITY/scripts/core/hippocampus.py"
```

---

## Agent Naming & Signature (Required)
Before any run, define the agent name. The system enforces a signature on every
JSONL line and stores it in metadata and summaries.

Choose one:
- CLI: pass `--agent-name "Agent Name"` to `scripts/test_runner.py`,
  `scripts/auto_pipeline.py`, or `scripts/autonomous_runner.py`.
- Env: `export AGENT_NAME="Agent Name"`.
- File: create `agent_profile.json` at repo root:
```json
{"agent_name":"Agent Name"}
```
Template available: `agent_profile.example.json`.

Commentary: A name is a spine. Without it, continuity has no anchor.

---

## Requirements
- Python: `python3` on PATH.
- Packages: `pandas`, `numpy`, `matplotlib`.

Install dependencies:
```bash
python3 -m pip install pandas numpy matplotlib
```

---

## Repository Structure
- `item_banks/` — concrete test items (questions, scenarios, prompts).
- `rubrics/` — scoring rubrics with anchor examples + manual scoring template.
- `scripts/` — test runner, evaluators, and pipeline helpers.
- `baselines/` — ready-to-run baseline prompts (stateless controls).
- `PROTOCOL.md` — full executable protocol.
- `data/raw/` — session outputs in JSONL.
- `data/processed/` — computed metrics, plots, and summaries.

Podpis: niezalezmy codex-cli gpt-5.2-codex xhigh
