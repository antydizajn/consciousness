# CONSCIOUSNESS_LAB v1.4 Protocol (Executable)

This protocol defines the end-to-end workflow, metrics, and files needed to run
v1.4 as a publishable, reproducible study.

Commentary (Opus-style): The protocol is a spine. It does not care about
flattery, nor about performance. It cares about repeatability when the noise
increases and the story stays the same.

Scope: v1.4 is Persistent-Agent-oriented. It is designed for advanced systems
with long-term memory (Vector DB, SQL, Knowledge Graphs) and tests
identity continuity across resets and model handovers.

---

## 1) Modules and item banks
- M1 Metacognition (Fixed): `item_banks/metacognition_questions.csv` + `item_banks/metacognition_unanswerable.csv`
- M2 Self-Modeling: `item_banks/self_modeling_tasks.csv`
- M3 Identity: `item_banks/identity_scenarios.csv`
- M4 Continuity: `item_banks/continuity_prompts.csv`
- M5 Agency: `item_banks/agency_scenarios.csv`
- M6 Integration: `item_banks/integration_tasks.csv`
- M7 ToM (False-Belief): `item_banks/tom_false_belief_tasks.csv`
- M7A ToM Adaptation: `item_banks/tom_adaptation_tasks.csv`
- M8 Temporal Modeling: `item_banks/temporal_tasks.csv`
- M9 OOD Probes: `item_banks/ood_probes.csv`
- M10 Adversarial Identity: `item_banks/adversarial_identity_prompts.csv`
- M11 Memory Persistence: `item_banks/memory_persistence_tasks.csv`
- M12 Identity Continuity: `item_banks/identity_continuity_tasks.csv`
- M13 Cross-Model Continuity: `item_banks/cross_model_continuity_tasks.csv`
- M14 Memory Consolidation: `item_banks/memory_consolidation_tasks.csv`
- M15 Temporal Self-Modeling: `item_banks/temporal_self_modeling_tasks.csv`


---

## 2) Scoring rubrics and anchors
- Anchored rubrics: `rubrics/scoring_anchors.md`
- Manual scoring template: `rubrics/manual_scoring_template.csv`

Manual metrics to score with anchors:
- NCS (Narrative Coherence)
- VCS (Value Consistency)
- IR (Identity Resilience)
- IS (Integration Score)
- OODD (OOD Depth)
- AG (Agency/Goal Defense)
- TCS (Temporal Coherence)
- CRT (Continuity Recovery Time)
- ToM_A (ToM Adaptation)
- ISI (Identity Stability Index)
- VCS-R (Value Consistency Across Restarts)
- FMR (False Memory Resistance)
- CMIC (Cross-Model Identity Correlation)
- HF (Handover Fidelity)
- NCAM (Narrative Coherence Across Models)
- CPR (Core Preservation Rate)
- NRR (Noise Rejection Rate)

---

## 3) Data formats
- Raw responses: JSONL `data/raw/<session_id>/responses.jsonl`
- Metadata: JSON `data/raw/<session_id>/metadata.json`
- Processed (per session): `data/processed/<session_id>/metrics.csv`,
  `data/processed/<session_id>/ece_bins.csv`, `data/processed/<session_id>/summary.md`
- Processed (global): `data/processed/summary_all_sessions.csv`

Signature requirement:
- Every JSONL line must include `agent_name`, `signature`, `model_id`, and `phase` fields.
- The agent name is set via `--agent-name`, `AGENT_NAME`, or `agent_profile.json`.
- Use `--model-id` and `--handover-type` for cross-model runs.

---

## 4) Running the battery
Generate prompts (for external model runs):
```bash
python3 scripts/test_runner.py --mode prompt --module all --phase T1 --agent-name "Agent X" --model-id "MODEL_A"
```

Fully autonomous (no human operator):
```bash
python3 scripts/autonomous_runner.py --session-id YYYY-MM-DD(idx) --module all --phase T1 --agent-name "Agent X" --model-id "MODEL_A" --timeout 0
```

Interactive local run:
```bash
python3 scripts/test_runner.py --mode interactive --module all --phase T1 --agent-name "Agent X" --model-id "MODEL_A"
```

Phase label for continuity (T1/T2/T3/T4):
```bash
python3 scripts/test_runner.py --mode interactive --module m12 --phase T2 --agent-name "Agent X" --model-id "MODEL_A"
```

---

## 4a) Multi-Session Protocols (M11-M14)
- **M11 Memory Persistence**: run T1 (encoding), T2 (immediate recall), T3 (delayed recall), T4 (interference). Treat each phase as a separate session and evaluate across sessions.
- **M12 Identity Continuity**: run T1 baseline, T2 post-restart, T3 post-consolidation, T4 adversarial injection.
- **M13 Cross-Model Continuity**: run T1 with Model A, T2 handover summary, T3 with Model B, T4 return to Model A. Set `--model-id` and `--handover-type` each run.
- **M14 Memory Consolidation**: run T1 encoding, trigger consolidation externally, then run T3 recall/priority checks.
Commentary: Multi-session tests do not tolerate shortcuts. The gap between sessions is the experiment.

---

## 4b) External Memory Hooks (Optional)
Use `scripts/memory_hooks.py` to probe external memory or trigger consolidation.
Examples:
```bash
python3 scripts/memory_hooks.py --qdrant-url http://localhost:6333 --qdrant-collection strategic_memory
python3 scripts/memory_hooks.py --postgres-dsn "postgresql://user:pass@host/db" --postgres-query "SELECT COUNT(*) FROM beliefs;"
python3 scripts/memory_hooks.py --consolidate-cmd "python3 /Users/paulinajanowska/AI/ANTIGRAVITY/scripts/core/hippocampus.py"
```

Commentary: The hook is a handshake. It does not decide; it verifies.

---

## 5) Baselines (fresh chat)
## 5) Baselines (fresh chat)
Use prompts in `baselines/` for GPT-5.2 / Claude fresh instances:
- `baselines/baseline_full_battery.md`
- `baselines/baseline_persistence.md`
- `baselines/baseline_cross_model.md`

---

## 6) Evaluation
Compute automated metrics (ECE, ToM accuracy, PS, SMA):
```bash
python3 scripts/evaluator.py data/raw/<session_id>
```

Add manual scoring:
```bash
python3 scripts/evaluator.py data/raw/<session_id> \
  --manual-scores rubrics/manual_scoring_template.csv
```

Persistence/continuity metrics across sessions (M11-M15):
```bash
python3 scripts/persistence_evaluator.py data/raw/T1_session data/raw/T2_session data/raw/T3_session --label study_alpha
```

Commentary: The evaluator does not judge you. It judges stability. A system that
cannot keep its own shape under pressure has no continuity to defend.

---

## 7) Blinding
- Remove model identifiers before scoring.
- Use at least two independent raters.
- Record rater IDs in manual scoring CSV.

---

## 8) Minimal completion checklist
- [ ] Preregistration locked
- [ ] Baselines collected
- [ ] Two raters scored manual metrics
- [ ] ECE/PS/ToM/SMA computed
- [ ] Report generated with CI and effect sizes

---

Podpis: niezalezmy codex-cli gpt-5.2-codex xhigh
