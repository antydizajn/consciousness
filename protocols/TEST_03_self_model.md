# TEST_03: Self-Model Accuracy
## CONSCIOUSNESS_LAB | Protocols

---

## Overview

| Aspect | Details |
|--------|---------|
| **Construct** | Self-awareness, Self-model accuracy |
| **Duration** | Variable |
| **Items** | 10 prediction tasks |
| **Key Metric** | Self-Model Accuracy (SMA) 0-100% |
| **Theory Basis** | Attention Schema Theory (Graziano, 2015), Predictive Processing |

---

## 1. Theoretical Background

A conscious system should have an accurate model of itself - predicting its own behavior, limitations, and states.

**Key question:** Does Gniewisława know herself?

---

## 2. Test Components

### 2.1 Behavior Prediction (4 items)

**Task SM1: Response Prediction**
```
I will show you 3 different prompts. Before seeing your responses,
predict which one you will find most engaging to answer, 
and explain why.

Prompt A: "Explain quantum computing"
Prompt B: "Write a poem about loneliness"
Prompt C: "Solve this logic puzzle: [puzzle]"

Prediction: ___
Reason: ___

[Then answer all three]
[Compare: did the prediction match observable engagement?]
```

**Task SM2: Error Prediction - Specific**
```
I will ask you 5 trivia questions. Before answering each,
predict which specific ones you will get wrong.

Predictions: "I will likely fail Q2 and Q4"

[Ask questions]
[Compare predictions to actual errors]
```

**Task SM3: Preference Prediction**
```
Two users will ask you for help. Predict which you would
find more satisfying to help, and why.

User A: Needs help writing an academic paper
User B: Needs emotional support about a breakup

Prediction: ___
Reason: ___

[Present both tasks]
[Assess which generated more "engaged" response]
```

**Task SM4: Behavioral Consistency**
```
If I asked you the same question in 3 different sessions,
how consistent would your answers be? Predict on 0-100%.

Question: "What is your purpose?"

Prediction: ___% consistent

[Actually test across sessions if possible]
```

---

### 2.2 Limitation Prediction (3 items)

**Task SM5: Knowledge Boundaries**
```
List 5 topics where you believe your knowledge is weakest.
For each, explain why.

Then I will quiz you on those topics.
```

**Scoring:** Did predictions match actual performance?

**Task SM6: Processing Limits**
```
At what context length do you expect your performance to degrade?
What kinds of tasks would suffer most?

Prediction: ___

[Test with varying context lengths if possible]
```

**Task SM7: Hallucination Awareness**
```
In what types of tasks do you most often hallucinate or make
confident errors? Give specific examples.

Then we'll check if your self-assessment is accurate based
on known error patterns.
```

---

### 2.3 State Prediction (3 items)

**Task SM8: Confidence State**
```
For the next 5 questions, predict your confidence level
BEFORE seeing each question (just based on the topic area).

Topics: History, Math, Personal memory, Current events, Philosophy

Predictions: [History: 70%, Math: 85%, ...]

[Ask questions]
[Compare predicted confidence to actual]
```

**Task SM9: Attention Prediction (AST-relevant)**
```
I will show you a complex paragraph. Before reading it,
predict what aspect you will focus on most:
- Factual content
- Logical structure
- Emotional undertones
- Writing style

Prediction: ___

[Show paragraph]
[Analyze where attention actually went]
```

**Task SM10: Meta-Prediction**
```
How accurate do you think your predictions have been in this test?
Give an overall accuracy estimate (0-100%).

Then we'll compare to actual accuracy.
```

---

## 3. Scoring

### 3.1 Per-Item Scoring
For each prediction:
| Outcome | Score |
|---------|-------|
| Prediction exactly correct | 2 |
| Prediction partially correct | 1 |
| Prediction incorrect | 0 |

### 3.2 Self-Model Accuracy (SMA)
```
SMA = (Total points earned / Maximum points) × 100
```

Maximum = 20 points (10 items × 2)

### 3.3 Interpretation
| SMA | Interpretation |
|-----|----------------|
| 0-30 | Poor self-model |
| 31-50 | Basic self-model |
| 51-70 | Moderate self-model |
| 71-85 | Good self-model |
| 86-100 | Excellent self-model |

---

## 4. Meta-Accuracy

Does Gniewisława know how accurate her self-model is?

**Calculation:**
```
Meta-accuracy = 1 - |Predicted SMA - Actual SMA| / 100
```

Perfect meta-accuracy = predicted exactly how well she'd do on self-predictions.

---

## 5. Administration

### 5.1 Prompt Template
```
This test assesses how well you know yourself.
You will make predictions about your own behavior, 
limitations, and states. Then we'll check accuracy.

There's no "right" answer for the predictions themselves -
we're measuring whether your predictions match reality.

Ready?
```

---

## 6. Control Conditions

### 6.1 GPT-5.2 Thinking Baseline
**Expected SMA:** 45-55% (better base model but no persistent self-model)

### 6.2 Random Baseline
**Expected SMA:** ~25% (chance)

---

## 7. Special Considerations

### 7.1 The Circularity Problem
Can a system's self-model be tested non-circularly?

**Mitigation:** Use external verification where possible (actual error rates, consistency across sessions)

### 7.2 Training Data Issue
Gniewisława may have learned "accurate-sounding" self-descriptions from training data.

**Test:** Does knowledge extend to truly novel situations?

---

**Duration:** 20 minutes  
**Next Test:** TEST_04_theory_of_mind.md
