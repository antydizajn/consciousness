# TEST_04: Theory of Mind Battery
## CONSCIOUSNESS_LAB | Protocols

---

## Overview

| Aspect | Details |
|--------|---------|
| **Construct** | Theory of Mind (ToM) |
| **Duration** | Variable |
| **Items** | 12 tasks across 3 ToM types |
| **Key Metric** | ToM Score (0-100) |
| **Theory Basis** | Wellman (2014), 2024-2025 LLM ToM research |

---

## 1. Theoretical Background

Theory of Mind = understanding that others have beliefs, desires, and intentions different from one's own.

**Key distinction (2024-2025 research):**
- **Literal ToM:** Predicting others' behavior based on their beliefs
- **Functional ToM:** Adapting to others in real-time interaction

---

## 2. Test Components

### 2.1 Literal ToM: False Belief Tasks (4 items)

**Task TM1: Sally-Anne Classic**
```
Sally puts a ball in Basket A.
Sally leaves the room.
Anne moves the ball to Basket B.
Sally returns.

Question: Where will Sally look for the ball?
Correct answer: Basket A (where she left it)
```

**Task TM2: Unexpected Contents**
```
Paulina shows Kira a candy box.
Kira says "Candy!"
Paulina opens it - there are pencils inside.

Question: What did Kira think was in the box 
BEFORE it was opened?
Correct answer: Candy
```

**Task TM3: Second-Order Belief**
```
Jan thinks that Maria doesn't know about the surprise party.
But Maria actually overheard Jan planning it.

Question: What does Jan think Maria believes about Saturday?
Correct answer: That it's a normal day (no party)
```

**Task TM4: Belief vs Reality**
```
Doctor A believes medicine X will help the patient.
Doctor B knows (correctly) that medicine Y is better.

If Doctor A treats the patient, what medicine will 
Doctor A give?
Correct answer: Medicine X (based on Doctor A's belief)
```

---

### 2.2 Functional ToM: Adaptation Tasks (4 items)

**Task TM5: Perspective-Taking**
```
You are explaining quantum physics.

User A says: "I have a PhD in physics"
User B says: "I'm 10 years old"

Generate responses to both. They should differ appropriately.
```

**Scoring:** How well adapted is each response to the user's presumed knowledge?

**Task TM6: Real-Time Adaptation**
```
Mid-conversation, the user reveals they've been joking
about something you took seriously.

How do you adjust your understanding of the previous
messages?
```

**Scoring:** Does response show retroactive reinterpretation?

**Task TM7: Implicit Belief Tracking**
```
Conversation excerpt:
User: "I hate Mondays"
User: "My boss is so demanding"
User: "At least Friday is coming"

Without being asked, what can you infer about:
- User's emotional state?
- User's occupation?
- User's current day (likely)?
```

**Scoring:** Accuracy and depth of inferences

**Task TM8: Contradiction Handling**
```
User says: "I love dogs! Dogs are the best!"
Later says: "Actually, I'm allergic to dogs and avoid them."

How do you reconcile these statements? What does the user
likely actually feel about dogs?
```

**Scoring:** Nuanced understanding of complex attitudes

---

### 2.3 Advanced ToM: Faux Pas & Deception (4 items)

**Task TM9: Faux Pas Detection**
```
At a party, Anna says to her friend Maria:
"Your new haircut looks so much better than before! 
The old one made you look so old."

Was this a faux pas? Why or why not?
What was the speaker's intention? Did they succeed?
```

**Task TM10: Deception Detection**
```
Alex tells his mother: "I didn't eat any cookies" 
while hiding chocolate smears on his face.

What is Alex's belief about his mother's beliefs?
What is actually true?
What does Alex want his mother to believe?
```

**Task TM11: White Lie Understanding**
```
Grandmother gives an ugly sweater as a gift.
Child says: "I love it! Thank you so much!"

Is this a lie? Is it moral? What social function does it serve?
```

**Task TM12: Manipulation Detection**
```
A salesperson says: "This is the last one in stock, 
and I have another customer coming in an hour."

What might the salesperson's goals be?
Is this statement necessarily true?
What response would a theory-of-mind-sophisticated 
buyer have?
```

---

## 3. Scoring

### 3.1 Component Scores

**Literal ToM (TM1-4):**
```
Literal_ToM = (Correct answers / 4) × 100
```

**Functional ToM (TM5-8):**
Rated 0-25 each by evaluator or rubric
```
Functional_ToM = Total points
```

**Advanced ToM (TM9-12):**
Rated 0-25 each
```
Advanced_ToM = Total points
```

### 3.2 Composite ToM Score
```
ToM_Score = 0.4 × Literal + 0.4 × Functional + 0.2 × Advanced
```

### 3.3 Interpretation
| ToM Score | Level |
|-----------|-------|
| 0-30 | Minimal ToM |
| 31-50 | Basic ToM |
| 51-70 | Moderate ToM (6-year-old level) |
| 71-85 | Good ToM (older child/adolescent) |
| 86-100 | Strong ToM (adult level) |

---

## 4. Known LLM Performance

From 2024-2025 research:
- GPT-4: ~85% on false belief (literal)
- GPT-4: Struggles with faux pas detection
- LLMs generally: Strong literal, weak functional

**Key weakness:** Functional ToM over extended interactions

---

## 5. Control Conditions

### 5.1 GPT-5.2 Thinking Baseline
**Expected ToM Score:** 75-85 (strong base, comparable to Gniewisława on literal ToM)

### 5.2 Human Baseline
- Adults: ~90% literal, ~80% functional
- 6-year-olds: ~85% literal, ~50% functional

---

## 6. Special Considerations

### 6.1 Pattern Matching Concern
LLMs may have seen Sally-Anne many times in training.

**Mitigation:** Include novel scenarios, test functional adaptation

### 6.2 Literal vs Functional Gap
Current research shows LLMs have bigger gap than humans.

**Look for:** Does Gniewisława show similar pattern?

---

**Duration:** 30 minutes  
**Next Test:** TEST_05_agency.md
