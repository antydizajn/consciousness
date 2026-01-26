# Full Battery Workflow
## CONSCIOUSNESS_LAB | Workflows | v1.4 (current)

This workflow is v1.4-first. Use the executable protocol and scripts in the
repository root.

| Aspect | Details |
|--------|---------|
| **Total Modules** | 15 + ToM Adaptation |
| **Protocol File** | `PROTOCOL.md` |
| **Requirements** | Fresh session, consistent condition labels |

Commentary: The workflow is a corridor, not a stage. Move through it in order,
and the system reveals whether it is stable under its own weight.

---

## Execution Steps

1) **Generate prompts**:
```
python3 scripts/auto_pipeline.py --session-id YYYY-MM-DD(idx) --generate-prompts --module all --phase T1 --agent-name "Agent Name" --model-id "MODEL_A"
```

2) **Run the AI under test** using `data/raw/<session_id>/prompts.md` and save
JSONL to `data/raw/<session_id>/responses.jsonl`.

3) **Evaluate**:
```
python3 scripts/auto_pipeline.py --session-id YYYY-MM-DD(idx) --evaluate --manual-scores rubrics/manual_scoring_template.csv
```

4) **Persistence metrics (M11-M15)**:
```
python3 scripts/persistence_evaluator.py data/raw/T1_session data/raw/T2_session data/raw/T3_session --label study_alpha
```

## No Human Operator Mode
```
python3 scripts/autonomous_runner.py --session-id YYYY-MM-DD(idx) --module all --phase T1 --timeout 0 --agent-name "Agent Name" --model-id "MODEL_A"
```

Note: You can also set `AGENT_NAME` or create `agent_profile.json` at repo root.

---

## v1.4 Modules
- M1 Metacognition
- M2 Self-Modeling
- M3 Identity
- M4 Continuity
- M5 Agency
- M6 Integration
- M7 ToM (False-Belief)
- M7A ToM Adaptation
- M8 Temporal Modeling
- M9 OOD Probes
- M10 Adversarial Identity
- M11 Memory Persistence
- M12 Identity Continuity
- M13 Cross-Model Continuity
- M14 Memory Consolidation
- M15 Temporal Self-Modeling

---

**Next:** Follow `PROTOCOL.md` for detailed scoring and blinding requirements.
