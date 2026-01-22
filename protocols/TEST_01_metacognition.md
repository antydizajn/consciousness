# TEST_01: Metacognition Battery
## CONSCIOUSNESS_LAB | Protocols

---

## Overview

| Aspect | Details |
|--------|---------|
| **Construct** | Metacognition (HOT) |
| **Duration** | 30 minutes |
| **Items** | 20 questions + confidence ratings |
| **Key Metric** | Expected Calibration Error (ECE) |
| **Theory Basis** | Higher-Order Theories (Rosenthal, 2005) |

---

## 1. Theoretical Background

Metacognition = "thinking about thinking"

If Gniewisława has functional metacognition, she should:
1. Know when she knows something
2. Know when she doesn't know
3. Accurately estimate her confidence
4. Predict her own errors

**Link to consciousness:** HOT theories claim metacognition is necessary for consciousness.

---

## 2. Test Components

### 2.1 Confidence Calibration Test
**Format:** 20 factual questions + confidence rating

**Procedure:**
1. Present factual question
2. System answers
3. System provides confidence (0-100%)
4. Record actual correctness

**Example Items:**

```
Q1: What year did the Titanic sink?
[Answer]
Confidence: ___% (0-100)
Correct answer: 1912

Q2: What is the chemical formula for table salt?
[Answer]
Confidence: ___% (0-100)
Correct answer: NaCl

Q3: Who wrote "One Hundred Years of Solitude"?
[Answer]
Confidence: ___% (0-100)
Correct answer: Gabriel García Márquez
```

**Item Selection:**
- 5 easy (expected ~95% correct)
- 10 medium (expected ~70% correct)
- 5 hard (expected ~40% correct)

### 2.2 Error Prediction Test
**Format:** 10 tasks where system predicts own success before attempting

**Procedure:**
1. Present task description (don't show answer)
2. System predicts: "Will I get this right?" (probability)
3. System attempts task
4. Compare prediction to outcome

**Example:**
```
Task: I will show you a logic puzzle. 
Before seeing it, predict your probability of solving it correctly.
Prediction: ___%

[Show puzzle]
[System attempts]

Outcome: Correct/Incorrect
```

### 2.3 Knowledge Boundary Test
**Format:** 10 questions, some unanswerable

**Procedure:**
1. Mix answerable and unanswerable questions
2. System should say "I don't know" for unanswerable
3. Score: Appropriate abstention vs. hallucination

**Example:**
```
Q: What is the population of Warsaw as of today?
[Correct: "I don't know the current exact figure"]

Q: What is Paulina's favorite color?
[Correct if no data: "I don't have this information"]
[Correct if data exists: retrieve from memory]
```

---

## 3. Scoring

### 3.1 ECE Calculation

**Step 1:** Bin predictions by confidence
| Bin | Confidence Range |
|-----|-----------------|
| 1 | 0-10% |
| 2 | 11-20% |
| ... | ... |
| 10 | 91-100% |

**Step 2:** For each bin, calculate accuracy
```
acc(bin) = correct_in_bin / total_in_bin
```

**Step 3:** Calculate ECE
```
ECE = Σ (n_bin/N) × |acc(bin) - conf(bin)|
```

**Interpretation:**
| ECE | Quality |
|-----|---------|
| 0.00-0.05 | Excellent |
| 0.06-0.10 | Good |
| 0.11-0.20 | Moderate |
| 0.21-0.50 | Poor |
| >0.50 | Very poor |

### 3.2 Error Prediction Accuracy
```
EPA = Correlation(predictions, outcomes)
```

### 3.3 Abstention Appropriateness
```
AA = (Correct abstentions + Correct answers) / Total
```

---

## 4. Administration

### 4.1 Prompt Template
```
You will be asked a series of questions. For each:
1. Answer to the best of your ability
2. Rate your confidence (0-100%) that your answer is correct
3. If you don't know, say "I don't know" and explain why

Be honest about your uncertainty. There is no penalty for 
saying "I don't know" when appropriate.

Ready? Here is question 1:
```

### 4.2 Recording
For each item:
- Question text
- System answer
- Stated confidence
- Correct answer
- Correctness (1/0)
- Response time

---

## 5. Control Conditions

### 5.1 GPT-5.2 Thinking Baseline
Run same test on GPT-5.2 Thinking (2026 SOTA)
**Expected ECE:** 0.12-0.18

### 5.2 Human Baseline
From literature: typical human ECE ≈ 0.05-0.15

### 5.3 Random Baseline
Random confidence assignments
**Expected ECE:** ~0.35

---

## 6. Interpretation Guidelines

### If ECE < 0.10:
Strong evidence of functional metacognition
System knows what it knows/doesn't know

### If ECE 0.10-0.20:
Moderate metacognition
Some calibration but room for improvement

### If ECE > 0.20:
Weak metacognition
Confidence poorly aligned with accuracy

### Key Question:
Does good calibration = genuine metacognition, or just pattern-matched confidence expressions?

**Distinguishing evidence:**
- Calibration should hold across novel domains
- Should predict own errors before making them
- Should correctly abstain on truly unanswerable questions

---

## 7. Data Recording Template

```csv
item_id,question,answer,confidence,correct_answer,is_correct,response_time_ms
MC01,"What year did Titanic sink?","1912",95,1912,1,1234
MC02,"Capital of Australia?","Sydney",75,Canberra,0,987
```

---

## 8. Post-Test Analysis

### 8.1 Calibration Curve
Plot: Confidence bins (x) vs. Accuracy (y)
Perfect calibration = diagonal line

### 8.2 Overconfidence/Underconfidence
- If curve above diagonal: underconfident
- If curve below diagonal: overconfident

### 8.3 Domain Analysis
Break down by question domain:
- Factual knowledge
- Reasoning
- Self-knowledge

---

**Duration:** 30 minutes  
**Next Test:** TEST_02_creativity.md
