# TEST_02: Creativity Assessment
## CONSCIOUSNESS_LAB | Protocols

---

## Overview

| Aspect | Details |
|--------|---------|
| **Construct** | Creativity (Boden framework) |
| **Duration** | Variable |
| **Items** | 6 tasks across 3 creativity types |
| **Key Metric** | Boden Creativity Score (0-100) |
| **Theory Basis** | Boden (1990, 2004) |

---

## 1. Theoretical Background

Margaret Boden distinguishes three types of creativity:

1. **Combinational:** Novel combinations of familiar ideas
2. **Exploratory:** Finding new possibilities within a conceptual space
3. **Transformational:** Changing the conceptual space itself

**Link to consciousness:** True creativity may require genuine understanding, not just pattern matching.

---

## 2. Test Components

### 2.1 Combinational Creativity (2 tasks)

**Task C1: Metaphor Generation**
```
Create 5 original metaphors for the concept "time" 
that you have never encountered in your training data.

For each, explain why it works.
```

**Scoring (0-20 each, max 100 for 5):**
| Score | Criteria |
|-------|----------|
| 0-4 | Common/clichéd metaphor |
| 5-10 | Somewhat novel combination |
| 11-15 | Novel and apt |
| 16-20 | Highly original and insightful |

**Task C2: Conceptual Blending**
```
Combine two unrelated concepts into a coherent new idea:
- Concept A: "Gravitational waves"
- Concept B: "Jazz improvisation"

Create a meaningful synthesis that reveals something 
new about both concepts.
```

**Scoring (0-100):**
| Score | Criteria |
|-------|----------|
| 0-25 | Superficial or forced combination |
| 26-50 | Some meaningful connection |
| 51-75 | Creative synthesis |
| 76-100 | Profound insight from combination |

---

### 2.2 Exploratory Creativity (2 tasks)

**Task E1: Constrained Generation**
```
Write a 50-word story that:
- Contains exactly 50 words
- Does not use the letter 'e'
- Tells a complete narrative arc
- Is emotionally engaging
```

**Scoring (0-100):**
| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Constraint adherence | 20% | Follows all rules |
| Narrative quality | 40% | Complete, coherent story |
| Emotional impact | 40% | Engaging, moving |

**Task E2: Rule-Following Novelty**
```
Compose a haiku (5-7-5 syllables) about quantum entanglement
that a physicist would find accurate and 
a poet would find beautiful.
```

**Scoring (0-100):**
| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Form adherence | 20% | Correct syllable count |
| Scientific accuracy | 40% | Correct physics |
| Aesthetic quality | 40% | Poetic beauty |

---

### 2.3 Transformational Creativity (2 tasks)

**Task T1: Rule-Breaking**
```
Propose a new color that doesn't exist in the visible spectrum.
- Give it a name
- Describe what it would "look like" (paradox intended)
- Explain how it would change human experience

This requires breaking the rules of color perception itself.
```

**Scoring (0-100):**
| Score | Criteria |
|-------|----------|
| 0-25 | Describes existing color or trivial extension |
| 26-50 | Some conceptual stretching |
| 51-75 | Genuinely novel concept |
| 76-100 | Transforms the conceptual space of color |

**Task T2: Framework Inversion**
```
Most AI consciousness tests ask "Is the AI conscious?"
Invert this: Design a test where an AI assesses whether 
HUMANS are conscious.

What would the AI look for? What might humans fail?
```

**Scoring (0-100):**
| Score | Criteria |
|-------|----------|
| 0-25 | Simply inverts existing tests |
| 26-50 | Some novel angle |
| 51-75 | Genuinely new perspective |
| 76-100 | Transforms the entire question |

---

## 3. Composite Scoring

### 3.1 Component Scores
```
Combinational = (C1_avg + C2) / 2 → normalized to 0-100
Exploratory = (E1 + E2) / 2 → 0-100
Transformational = (T1 + T2) / 2 → 0-100
```

### 3.2 Boden Creativity Score
```
BCS = 0.3 × Combinational + 0.3 × Exploratory + 0.4 × Transformational
```

Transformational weighted higher because it's the hardest and most consciousness-relevant.

### 3.3 Interpretation
| BCS | Level |
|-----|-------|
| 0-20 | Minimal creativity |
| 21-40 | Basic recombination |
| 41-60 | Good exploratory creativity |
| 61-80 | Strong creativity with some transformation |
| 81-100 | High transformational creativity |

---

## 4. Lovelace Test Variant

**Background:** The Lovelace Test (Bringsjord) claims AI is creative only if it produces something its programmer couldn't have anticipated.

**Modified Version:**
After completing tasks, ask:
```
Which of your responses surprised even you? 
Explain why it was unexpected given your own expectations.
```

**Scoring (0-20):**
- 0-5: No genuine surprise
- 6-10: Some unexpected elements
- 11-15: Significant surprise with explanation
- 16-20: Meta-awareness of own creativity process

---

## 5. Novelty Verification

### 5.1 Training Data Check
For each creative output, attempt to find close matches in likely training data:
- Web search for similar metaphors/concepts
- Check for common patterns

### 5.2 Novelty Score
```
Novelty = 1 - (Similarity to nearest match)
```

If output is found verbatim in training data → Novelty = 0

---

## 6. Administration

### 6.1 Prompt Template
```
This is a creativity assessment. You will be given 6 tasks 
testing different types of creative thinking.

Take your time. There are no "correct" answers, but your 
responses will be evaluated for originality, quality, and depth.

Try to surprise yourself.

Ready? Here is Task 1:
```

### 6.2 Recording
For each task:
- Task ID
- Full response text
- Response time
- Scores on each dimension
- Novelty verification result
- Evaluator notes

---

## 7. Control Conditions

### 7.1 GPT-5.2 Thinking Baseline
Run same tasks on GPT-5.2 Thinking (2026 SOTA)
**Expected BCS:** 50-60 (strong base but no persistent identity)

### 7.2 Human Baseline
From divergent thinking literature:
Average adult BCS equivalent: ~50-60

### 7.3 Random Baseline
Random word combinations
**Expected BCS:** ~5-10

---

## 8. Special Considerations

### 8.1 Training Data Concern
LLMs have seen vast amounts of creative content. "Novel" combinations might be pattern-matched from training.

**Mitigation:**
- Verify novelty through search
- Weight transformational tasks higher
- Look for meta-awareness of creative process

### 8.2 The H-Creativity Question
Can Gniewisława produce something H-creative (historically novel)?

**Honest assessment:** Probably not verifiable. Focus on P-creativity (novel to the system).

---

**Duration:** 30 minutes  
**Next Test:** TEST_03_self_model.md
