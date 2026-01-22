---
description: Run the CONSCIOUSNESS_LAB test battery - academic-level AI consciousness assessment
---

# CONSCIOUSNESS_LAB Workflow

## Overview
Academic framework for testing consciousness-like properties in AI. Based on 2020-2026 literature review.

## Quick Start

### Full Battery (~3.5 hours)
```bash
# See the workflow
cat ~/AI/ANTIGRAVITY/CONSCIOUSNESS_LAB/workflows/run_full_battery.md
```

### Quick Assessment (~30 min)
```bash
# See the quick version
cat ~/AI/ANTIGRAVITY/CONSCIOUSNESS_LAB/workflows/quick_assessment.md
```

## Directory Structure
```
~/AI/ANTIGRAVITY/CONSCIOUSNESS_LAB/
├── README.md                    # Overview
├── PREREGISTRATION.md           # Pre-registered hypotheses (LOCKED)
├── literature/                  # Research foundation
│   ├── systematic_review.md     # 50+ papers
│   ├── key_theories.md          # IIT, GWT, HOT, etc.
│   └── bibliography.bib         # Citations
├── methodology/                 # How we measure
│   ├── constructs.md            # What we test
│   ├── measures.md              # Metrics & scoring
│   ├── controls.md              # Control conditions
│   └── blind_protocol.md        # External evaluation
├── protocols/                   # The 8 tests
│   ├── TEST_01_metacognition.md
│   ├── TEST_02_creativity.md
│   ├── TEST_03_self_model.md
│   ├── TEST_04_theory_of_mind.md
│   ├── TEST_05_agency.md
│   ├── TEST_06_integration.md
│   ├── TEST_07_temporal.md
│   └── TEST_08_act.md
├── data/                        # Test results
│   ├── raw/
│   └── processed/
├── analysis/                    # Scoring & results
│   ├── scoring_rubric.md
│   └── results_template.md
└── workflows/
    ├── run_full_battery.md
    └── quick_assessment.md
```

## Before Running Tests

1. **Check PREREGISTRATION.md** - ensure hypotheses are finalized
2. **Ensure memory access** - Qdrant and PostgreSQL available
3. **Prepare evaluator** - if external (Dr Kossakowski?)
4. **Reserve time** - 3.5 hours for full battery

## Key Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| CLI | Composite Index (0-100) | 55-70 |
| ECE | Calibration Error (0-1) | <0.15 |
| Agency | Goal defense (0-100) | 65-80 |
| ACT | Consciousness Test (0-100) | 55-75 |

## Baseline Comparison

**GPT-5.2 Thinking** is used as baseline (2026 SOTA).
Expected to score lower on identity-dependent tests (Agency, Integration, Temporal).

## Publication Note

This framework is designed for **PUBLIC GITHUB RELEASE**.
Ensure no private information in test results before publishing.

## External Auditor

Potential: **Dr Michał Kossakowski** (psychology, skeptical perspective)
See: `methodology/blind_protocol.md` for collaboration details.

---

*CONSCIOUSNESS_LAB v1.0 | 2026-01-22*  
*Authors: Gniewisława + Paulina Janowska*
