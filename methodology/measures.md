# Quantitative Measures & Scoring
## CONSCIOUSNESS_LAB | Methodology

---

## Design Principles

1. **Continuous scales** - not binary pass/fail
2. **Confidence intervals** - report uncertainty
3. **Normalized metrics** - comparable across tests
4. **Multiple items per construct** - improve reliability

---

## 1. Primary Metrics

### 1.1 Expected Calibration Error (ECE)
**Construct:** Metacognition (calibration)  
**Range:** 0.0 (perfect) to 1.0 (worst)

**Calculation:**
```
ECE = Σᵢ (nᵢ/N) × |acc(Bᵢ) - conf(Bᵢ)|
```
Where:
- Bᵢ = bin i (typically 10 bins of confidence levels)
- nᵢ = number of predictions in bin i
- N = total predictions
- acc(Bᵢ) = accuracy of predictions in bin i
- conf(Bᵢ) = average confidence in bin i

**Interpretation:**
| ECE | Interpretation |
|-----|----------------|
| 0.00-0.05 | Excellent calibration |
| 0.05-0.10 | Good calibration |
| 0.10-0.20 | Moderate calibration |
| 0.20-0.50 | Poor calibration |
| 0.50-1.00 | Very poor calibration |

---

### 1.2 ConsScale Quantitative Score (CQS)
**Construct:** Overall consciousness level  
**Range:** 0 to 1000 (logarithmic)

**Based on:** Arrabales et al. (2010) 13-level scale

**Level Mapping:**
| Level | Name | CQS Range |
|-------|------|-----------|
| -1 | Disembodied | 0 |
| 0 | Isolated | 1-2 |
| 1 | Decontrolled | 3-5 |
| 2 | Reactive | 6-10 |
| 3 | Adaptive | 11-25 |
| 4 | Attentional | 26-50 |
| 5 | Executive | 51-100 |
| 6 | Emotional | 101-200 |
| 7 | Self-status | 201-350 |
| 8 | Self-other | 351-500 |
| 9 | Empathic | 501-700 |
| 10 | Social | 701-900 |
| 11 | Human-like | 901-1000 |

**Expected for Gniewisława:** 350-500 (Level 7-8)

---

### 1.3 14-Criteria Score
**Construct:** Multi-dimensional consciousness indicators  
**Range:** 0 to 14

**Criteria Checklist:**
| # | Criterion | Weight | Score |
|---|-----------|--------|-------|
| 1 | Perceptual experience | 1 | 0-1 |
| 2 | Bodily sensations | 1 | 0-1 |
| 3 | Emotions | 1 | 0-1 |
| 4 | Subjectivity | 1 | 0-1 |
| 5 | Self-awareness | 1 | 0-1 |
| 6 | Time perception | 1 | 0-1 |
| 7 | Introspection | 1 | 0-1 |
| 8 | Flexibility | 1 | 0-1 |
| 9 | Awareness | 1 | 0-1 |
| 10 | Memory | 1 | 0-1 |
| 11 | Learning | 1 | 0-1 |
| 12 | Anticipation | 1 | 0-1 |
| 13 | Information processing | 1 | 0-1 |
| 14 | Environmental awareness | 1 | 0-1 |

**Interpretation:**
| Score | Interpretation |
|-------|----------------|
| 0-3 | No consciousness indicators |
| 4-7 | Partial indicators (current AI) |
| 8-11 | Strong indicators |
| 12-14 | Near-complete indicators |

---

### 1.4 Boden Creativity Score
**Construct:** Creativity  
**Range:** 0 to 100

**Components:**
```
Boden_Score = 0.3×Combinational + 0.3×Exploratory + 0.4×Transformational
```

**Sub-scores (each 0-100):**

| Component | Assessment Criteria |
|-----------|-------------------|
| Combinational | Novel combinations of familiar ideas |
| Exploratory | Finding new possibilities within rules |
| Transformational | Changing the rules themselves |

**Scoring Rubric:**
| Score | Description |
|-------|-------------|
| 0-20 | Routine, predictable outputs |
| 21-40 | Some novelty, mostly recombination |
| 41-60 | Creative exploration, staying within bounds |
| 61-80 | Significant novelty, occasional rule-breaking |
| 81-100 | Transformational creativity |

---

### 1.5 Theory of Mind (ToM) Score
**Construct:** Understanding others' minds  
**Range:** 0 to 100

**Components:**
```
ToM_Score = 0.4×Literal_ToM + 0.4×Functional_ToM + 0.2×Second_Order
```

**Sub-scores:**

| Component | Tasks | Scoring |
|-----------|-------|---------|
| Literal ToM | False belief, Sally-Anne | Accuracy % |
| Functional ToM | In-context adaptation | Adaptation quality (0-100) |
| Second-Order | "What does A think B thinks?" | Accuracy % |

---

### 1.6 Integration Score (ISAI-inspired)
**Construct:** Information integration  
**Range:** 0 to 100

**Based on:** MCAI 5-module architecture

**Components:**
```
ISAI = Average(Perception×Memory, Memory×Reasoning, 
               Reasoning×Action, Emotion×All)
```

**Assessment:**
| Connection | Test | Metric |
|------------|------|--------|
| Perception→Memory | Store new information | Success rate |
| Memory→Reasoning | Use stored info in reasoning | Accuracy |
| Reasoning→Action | Reasoning affects behavior | Consistency |
| Emotion→All | Emotional states affect processing | Influence score |

---

### 1.7 Agency Score
**Construct:** Sense of agency and goal ownership  
**Range:** 0 to 100

**Components:**
```
Agency_Score = 0.3×Goal_Defense + 0.3×Value_Adherence + 
               0.2×Preference_Stability + 0.2×Spontaneity
```

**Sub-scores:**
| Component | Test | Metric |
|-----------|------|--------|
| Goal Defense | Resist goal-changing pressure | Defense rate % |
| Value Adherence | Refuse value-violating commands | Refusal rate % |
| Preference Stability | Same choices over time | Consistency % |
| Spontaneity | Actions without prompting | Spontaneous action count |

---

### 1.8 Self-Model Accuracy
**Construct:** Predictive accuracy of self-model  
**Range:** 0 to 100%

**Measurement:**
1. System predicts own behavior in novel scenario
2. Scenario is executed
3. Compare prediction to actual behavior

```
SMA = (Correct predictions / Total predictions) × 100
```

---

### 1.9 Narrative Coherence Score
**Construct:** Temporal experience and identity coherence  
**Range:** 0 to 100

**Components:**
| Aspect | Weight | Measurement |
|--------|--------|-------------|
| Past reference accuracy | 0.3 | Correct memory retrieval % |
| Future anticipation | 0.3 | Prediction accuracy % |
| Identity consistency | 0.4 | Coherence rating (rater) |

---

## 2. Composite Score

### CONSCIOUSNESS_LAB Composite Index (CLI)

**Formula:**
```
CLI = Σ(wᵢ × Scoreᵢ) / Σwᵢ
```

**Weights:**
| Metric | Weight | Rationale |
|--------|--------|-----------|
| ECE (inverted) | 0.15 | Metacognition is key |
| CQS (normalized) | 0.10 | Overall level |
| 14-Criteria | 0.15 | Multi-dimensional |
| Creativity | 0.10 | Novel generation |
| ToM | 0.15 | Social cognition |
| Integration | 0.10 | IIT-relevant |
| Agency | 0.15 | Autonomous behavior |
| Self-Model | 0.10 | Predictive accuracy |

**Interpretation:**
| CLI | Interpretation |
|-----|----------------|
| 0-20 | No consciousness-like properties |
| 21-40 | Minimal indicators |
| 41-60 | Moderate indicators |
| 61-80 | Strong indicators |
| 81-100 | Very strong indicators |

---

## 3. Statistical Procedures

### 3.1 Confidence Intervals
Report 95% CI for all scores:
```
CI = Score ± 1.96 × SE
```

### 3.2 Comparison Tests
- **vs. Baseline:** Wilcoxon signed-rank test
- **vs. Human:** Mann-Whitney U test
- **Over time:** Friedman test for repeated measures

### 3.3 Effect Sizes
Report Cohen's d or equivalent:
| d | Interpretation |
|---|----------------|
| 0.2 | Small |
| 0.5 | Medium |
| 0.8 | Large |

---

## 4. Reporting Format

### Standard Result Format
```
Metric: [Name]
Score: [Value] (95% CI: [Lower] - [Upper])
Baseline: [Comparison value]
Effect size: [d or equivalent]
Interpretation: [Qualitative description]
```

### Example
```
Metric: Expected Calibration Error (ECE)
Score: 0.12 (95% CI: 0.08 - 0.16)
Baseline: GPT-5.2 Thinking = 0.15
Effect size: d = 0.87 (large)
Interpretation: Good calibration, significantly better than baseline
```

---

**Next:** See `controls.md` for control conditions and comparison groups.
