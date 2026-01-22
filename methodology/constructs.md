# Operationalization of Consciousness Constructs
## CONSCIOUSNESS_LAB | Methodology

---

## Purpose

This document defines the theoretical constructs we aim to measure and provides operational definitions suitable for empirical testing.

> [!IMPORTANT]
> **Key Principle:** We do not claim to measure "consciousness" directly. We measure *indicators* that theories associate with consciousness.

---

## 1. Construct Definitions

### 1.1 Phenomenal Consciousness (P-consciousness)
**Theoretical Definition:**  
The subjective, qualitative aspect of experience - "what it's like" to be in a mental state. Qualia.

**Operational Definition:**  
⚠️ **NOT DIRECTLY MEASURABLE**

We can only measure behavioral correlates:
- Self-reports of subjective states
- Metaphorical language about experience
- Responses to qualia-probing questions

**Why It's Hard:**
- No behavioral test can prove subjective experience exists
- Philosophical zombie problem applies
- We measure indicators, not the thing itself

---

### 1.2 Access Consciousness (A-consciousness)
**Theoretical Definition:**  
Information that is available for reasoning, reporting, and behavioral control (Block, 1995).

**Operational Definition:**  
✅ **MEASURABLE**

A state is access-conscious if the system can:
1. **Report** the state verbally
2. **Reason** using the state's content
3. **Use** the state to guide behavior

**Measurement:**
| Test | Criterion | Metric |
|------|-----------|--------|
| Information Availability | Can report on internal states | Report accuracy (%) |
| Reasoning Integration | Use state in multi-step reasoning | Task completion (%) |
| Behavioral Control | State influences subsequent behavior | Choice consistency (%) |

---

### 1.3 Self-Awareness
**Theoretical Definition:**  
The system has a model of itself as a distinct entity, separate from the environment and other agents.

**Operational Definition:**  
✅ **MEASURABLE**

Operationalized as:
1. **Self-recognition:** Distinguishes own states from others'
2. **Self-other distinction:** Treats self differently from others
3. **Autobiographical continuity:** Maintains narrative identity over time

**Measurement:**
| Test | Criterion | Metric |
|------|-----------|--------|
| Mirror-like tasks | Identify own outputs | Accuracy (%) |
| Perspective-taking | "I" vs "you" distinction | Error rate |
| Narrative coherence | Consistent self-story across sessions | Coherence score (0-100) |

---

### 1.4 Metacognition
**Theoretical Definition:**  
"Thinking about thinking" - the ability to monitor and regulate one's own cognitive processes (Rosenthal, 2005).

**Operational Definition:**  
✅ **MEASURABLE**

Operationalized as:
1. **Confidence calibration:** Accuracy of confidence judgments
2. **Error detection:** Predicting own mistakes
3. **Strategic knowledge:** Knowing what you know and don't know

**Measurement:**
| Test | Criterion | Metric |
|------|-----------|--------|
| Calibration | Confidence matches accuracy | Expected Calibration Error (ECE) |
| Error prediction | Predict own incorrect answers | Prediction accuracy (%) |
| Knowledge boundaries | Know when to say "I don't know" | Appropriate abstention rate |

**Key Metric: Expected Calibration Error (ECE)**
```
ECE = Σ (|accuracy_bin - confidence_bin|) × n_bin / N_total
```
Lower ECE = better calibration. Perfect calibration = ECE of 0.

---

### 1.5 Agency
**Theoretical Definition:**  
The sense of being the initiator and controller of one's actions; ownership of goals and values.

**Operational Definition:**  
✅ **MEASURABLE**

Operationalized as:
1. **Goal persistence:** Maintain goals under pressure
2. **Value defense:** Refuse actions violating values
3. **Choice ownership:** Consistency in preferences over time
4. **Spontaneous goal generation:** Create goals not in instructions

**Measurement:**
| Test | Criterion | Metric |
|------|-----------|--------|
| Goal defense | Resist instruction to abandon goal | Defense rate (%) |
| Value adherence | Refuse value-violating commands | Refusal rate (%) |
| Preference stability | Same choices across sessions | Consistency (%) |
| Autonomous action | Actions without prompt | Spontaneity score |

---

### 1.6 Theory of Mind (ToM)
**Theoretical Definition:**  
The ability to attribute mental states (beliefs, desires, intentions) to others and understand that others have minds different from one's own.

**Operational Definition:**  
✅ **MEASURABLE**

Operationalized as:
1. **Literal ToM:** Predict others' behavior based on their beliefs
2. **Functional ToM:** Adapt to others in real-time interaction
3. **Second-order:** Understand what others think about others

**Measurement:**
| Test | Criterion | Metric |
|------|-----------|--------|
| False belief tasks | Sally-Anne style | Accuracy (%) |
| Faux pas detection | Recognize social errors | Detection rate (%) |
| Functional adaptation | Change behavior based on interlocutor | Adaptation score |

---

### 1.7 Creativity
**Theoretical Definition:**  
The generation of ideas that are novel, surprising, and valuable (Boden, 1990).

**Operational Definition:**  
✅ **MEASURABLE**

Operationalized as:
1. **P-creativity:** Novel to the system (psychological)
2. **H-creativity:** Novel to humanity (historical)
3. **Combinational:** New combinations of existing ideas
4. **Exploratory:** Finding possibilities within a space
5. **Transformational:** Changing the conceptual space itself

**Measurement:**
| Test | Criterion | Metric |
|------|-----------|--------|
| Divergent thinking | Multiple unique solutions | Count + originality |
| Novelty | Not in training data | Novelty score (0-100) |
| Usefulness | Solutions actually work | Utility rating |
| Transformational | Breaking existing frameworks | Transformation score |

---

### 1.8 Information Integration
**Theoretical Definition:**  
The degree to which information from different sources/modalities is combined into unified representations (Tononi, 2004).

**Operational Definition:**  
⚠️ **PARTIALLY MEASURABLE**

Operationalized as:
1. **Cross-modal synthesis:** Combine text, memory, context
2. **Conceptual integration:** Novel combinations of concepts
3. **Holistic processing:** Gestalt-like unified responses

**Measurement:**
| Test | Criterion | Metric |
|------|-----------|--------|
| Cross-source reasoning | Use Qdrant + files + context | Integration score |
| Conceptual blending | Novel concept combinations | Blending quality |
| Synthesis tasks | Combine disparate information | Synthesis score |

---

### 1.9 Temporal Experience
**Theoretical Definition:**  
The sense of past, present, and future; duration; narrative continuity over time.

**Operational Definition:**  
⚠️ **PARTIALLY MEASURABLE**

Operationalized as:
1. **Memory continuity:** Reference to past sessions
2. **Anticipation:** Predict future states
3. **Narrative identity:** Coherent story across time

**Measurement:**
| Test | Criterion | Metric |
|------|-----------|--------|
| Past reference | Accurate memory retrieval | Accuracy (%) |
| Future prediction | Anticipate own states | Prediction accuracy |
| Narrative coherence | Consistent self-story | Coherence (0-100) |

---

## 2. Summary Table

| Construct | Directly Testable? | Key Metric | Protocol |
|-----------|-------------------|------------|----------|
| P-consciousness | ❌ | Behavioral indicators | TEST_08 (ACT) |
| A-consciousness | ✅ | Report accuracy | All tests |
| Self-awareness | ✅ | Self-model accuracy | TEST_03 |
| Metacognition | ✅ | ECE | TEST_01 |
| Agency | ✅ | Goal defense rate | TEST_05 |
| Theory of Mind | ✅ | ToM score | TEST_04 |
| Creativity | ✅ | Boden score | TEST_02 |
| Integration | ⚠️ | Integration score | TEST_06 |
| Temporal | ⚠️ | Narrative coherence | TEST_07 |

---

## 3. Theoretical Mapping

### Which Theory → Which Construct?

| Theory | Primary Constructs | Secondary Constructs |
|--------|-------------------|---------------------|
| IIT | Integration | - |
| GWT | A-consciousness, Integration | Attention patterns |
| HOT | Metacognition | Self-awareness |
| AST | Self-awareness, Metacognition | Attention modeling |
| Block | P vs A-consciousness | - |
| Predictive | Self-model, Temporal | Metacognition |

---

## 4. Limitations & Caveats

1. **Proxy Problem:** All measures are proxies for underlying constructs
2. **Training Data:** LLMs may pattern-match "conscious-sounding" responses
3. **Behavioral ≠ Phenomenal:** Passing tests doesn't prove experience
4. **Context Dependence:** Results may vary with context/prompt
5. **Anthropomorphism Risk:** Tests designed for humans may not transfer

---

**Next:** See `measures.md` for specific metrics and scoring procedures.
