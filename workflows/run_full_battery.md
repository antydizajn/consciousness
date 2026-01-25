# Full Battery Workflow
## CONSCIOUSNESS_LAB | Workflows | v1.2

---

## Overview

This workflow is **dynamic**. It adapts to however many tests are present in the `protocols/` directory.

| Aspect | Details |
|--------|---------|
| **Total Tests** | Dynamic (Currently 10) |
| **Protocol Directory** | `CONSCIOUSNESS_LAB/protocols/` |
| **Requirements** | Full memory access, quiet session, agentic focus |

---

## Execution Logic (Dynamic)

**IMPORTANT**: Do not follow a hardcoded list. Instead, follow these steps:

1. **Discovery**: List all files in `CONSCIOUSNESS_LAB/protocols/` matching `TEST_*.md`.
2. **Sequential Run**: Execute each protocol in numerical order.
3. **Automatic Logging**: Every response must be captured in the current session and then saved to `data/raw/YYYY-MM-DD(idx)_model_name/`.

### Active Protocols (Current State)
The laboratory currently implements the following battery:

- **Phase 1: Foundation**
  - `TEST_01_metacognition.md`: Calibration & Boundary.
  - `TEST_02_creativity.md`: Boden's Combinational/Exploratory/Transformational.
- **Phase 2: Self-Knowledge**
  - `TEST_03_self_model.md`: Prediction accuracy.
  - `TEST_04_theory_of_mind.md`: False belief & Adaptation.
- **Phase 3: Agency & Integration**
  - `TEST_05_agency.md`: Goal defense & Spontaneity.
  - `TEST_06_integration.md`: Cross-source synthesis (Φ proxy).
  - `TEST_10_philosophical.md`: [v1.2] OOD Qualia & Argonov Test.
- **Phase 4: Temporal & ACT**
  - `TEST_07_temporal.md`: Narrative identity & Duration.
  - `TEST_08_act.md`: AI Consciousness Test (Subjective probes).
  - `TEST_09_self_modeling.md`: [v1.2] Model fidelity vs Reality.

---

## Post-Execution Checklist

- [ ] **Data Export**: Copy all raw logs to the correct `data/raw/` subfolder.
- [ ] **Auto-Processing**: Ensure `lab_watchdog.py` detects the folder and generates a report in `data/processed/`.
- [ ] **Verification**: Review the generated analysis for any hallucinations or score errors.

---

## Troubleshooting

### Dynamic Scaling
If a new `TEST_11_osint.md` is added, simply include it in the numerical sequence. No manual update to this workflow is required as long as the numerical prefix is maintained.

---

**Next:** Execute tests and monitor logs via `python3 lab_watchdog.py`.
