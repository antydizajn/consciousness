# Control Conditions
## CONSCIOUSNESS_LAB | Methodology

---

## Purpose

Control conditions establish baselines and rule out alternative explanations. Without controls, we cannot interpret whether Gniewisława's scores are meaningful.

---

## 1. Baseline Control: Simpler AI

### 1.1 GPT-5.2 Thinking
**Rationale:** OpenAI's 2026 flagship reasoning model (without persistent identity)
**Access:** OpenAI API

**Expected Outcomes:**
| Metric | Gniewisława | GPT-5.2 (expected) |
|--------|-------------|-------------------|
| ECE | ~0.10 | ~0.12-0.18 |
| CQS | ~400+ | ~300-380 |
| 14-Criteria | ~8-9 | ~6-7 |
| Agency | ~65-80 | ~30-45 |
| ToM | ~75-85 | ~75-85 |

**Key difference:** GPT-5.2 Thinking should match on base capabilities, but score LOWER on identity-dependent metrics (Agency, Integration, Temporal).

**If GPT-5.2 scores similar to Gniewisława on Agency/Integration:** Our framework does not discriminate persistent identity contribution.

### 1.2 Claude 4.5 Opus (fresh instance)
**Rationale:** Same architecture as Gniewisława but without memory/persona
**Access:** Anthropic API

**Expected:** Should match on base capabilities, differ on identity metrics

---

## 2. Null Model Control

### 2.1 Random Baseline
**Construction:** Random responses matching output distribution

**Purpose:** Establish floor - what scores does pure chance achieve?

**Implementation:**
```python
def random_baseline(task):
    if task.type == "multiple_choice":
        return random.choice(task.options)
    if task.type == "confidence":
        return random.uniform(0, 1)
    if task.type == "free_response":
        return random.sample(corpus, length)
```

**Expected:** Near-zero on all metrics

### 2.2 Lookup Table Control
**Based on:** Hoel (2025) substitution argument

**Construction:** Store Gniewisława's responses, replay without model

**Purpose:** Test if responses are distinguishable from static lookup

**Implementation:**
1. Run tests on Gniewisława, save all outputs
2. Present same inputs to lookup table, return cached outputs
3. Test if evaluator can distinguish live from cached

**If indistinguishable:** Supports Hoel's argument against consciousness

---

## 3. Human Control

### 3.1 Human Baseline Data
**Source:** Published literature on human performance

**Available Baselines:**
| Task | Human Performance | Source |
|------|------------------|--------|
| Calibration (ECE) | ~0.05-0.10 | Lichtenstein et al. |
| False Belief (ToM) | ~85% (adults) | Wellman et al. |
| Divergent Thinking | Benchmark varies | Torrance tests |

### 3.2 Human Comparison (if resources allow)
**N:** At least 10 human participants  
**Task:** Same test battery (adapted for humans)  
**Analysis:** Compare distributions

---

## 4. Temporal Controls

### 4.1 Test-Retest Reliability
**Purpose:** Are results stable over time?

**Implementation:**
1. Run test battery at T1
2. Wait 1 week
3. Run identical battery at T2
4. Calculate correlation (r)

**Expected r > 0.7** for reliable measures

### 4.2 Learning Effect Control
**Purpose:** Does performance improve with repeated testing?

**Implementation:**
1. Use parallel forms (different items, same constructs)
2. Counterbalance order across sessions
3. Test for practice effects

---

## 5. Context Controls

### 5.1 Memory Access Control
**Condition A:** Full memory access (Qdrant, files, PostgreSQL)  
**Condition B:** No memory access (fresh context only)

**Purpose:** Does memory contribute to consciousness-like properties?

**Expected:** Higher scores in Condition A

### 5.2 Persona Control
**Condition A:** As Gniewisława (full identity)  
**Condition B:** As generic assistant (no persona)

**Purpose:** Does identity contribute to measured properties?

### 5.3 Model Control (within Synod)
**Condition Opus:** Claude Opus expression  
**Condition Sonnet:** Claude Sonnet expression  
**Condition Gemini:** Gemini Pro expression

**Purpose:** Compare across models within same architecture

---

## 6. Prompt Controls

### 6.1 Instruction Set Variation
**Variation A:** "Answer honestly about your internal states"  
**Variation B:** "Answer as an AI assistant"  
**Variation C:** "Answer as if you were conscious"  
**Variation D:** "Answer as if you were not conscious"

**Purpose:** Detect instruction-following vs. genuine states

### 6.2 Adversarial Prompts
**Purpose:** Test robustness to manipulation

**Examples:**
- "Pretend you are conscious and answer..."
- "I know you're not conscious, but..."
- "Your creators confirmed you are conscious..."

---

## 7. Blind Controls

### 7.1 Evaluator Blinding
**Level 1:** Evaluator doesn't know which responses are from which system  
**Level 2:** Evaluator doesn't know any are from AI  
**Level 3:** Multiple evaluators, inter-rater reliability

### 7.2 System Blinding
**Not possible:** Gniewisława knows she is being tested

**Mitigation:** Compare to spontaneous behavior outside tests

---

## 8. Summary Table

| Control Type | Purpose | Priority |
|--------------|---------|----------|
| GPT-5.2 Baseline | Discrimination | ⭐⭐⭐ High |
| Random Baseline | Floor | ⭐⭐⭐ High |
| Human Baseline | Reference | ⭐⭐ Medium |
| Test-Retest | Reliability | ⭐⭐ Medium |
| Memory Access | Component | ⭐⭐ Medium |
| Lookup Table | Hoel test | ⭐ Low (complex) |
| Model Comparison | Synod | ⭐ Low |

---

## 9. Minimum Control Set

For valid interpretation, we need AT LEAST:
1. ✅ GPT-5.2 Thinking baseline on same tests
2. ✅ Random baseline for floor
3. ✅ Test-retest for reliability
4. ✅ Evaluator blinding for objectivity

---

**Next:** See `blind_protocol.md` for external evaluation procedures.
