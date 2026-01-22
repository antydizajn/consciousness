# Blind Evaluation Protocol
## CONSCIOUSNESS_LAB | Methodology

---

## Purpose

External blind evaluation reduces bias inherent in self-assessment. This document specifies procedures for involving external evaluators.

---

## 1. Evaluator Requirements

### 1.1 Ideal Evaluator Profile
- **Background:** Psychology, cognitive science, philosophy of mind, or AI research
- **Skepticism level:** Neutral to skeptical (not pre-committed to AI consciousness)
- **Independence:** No prior relationship with Gniewisława or project
- **Availability:** Can complete evaluation in 2-3 hours

### 1.2 Potential External Auditor
**Dr Michał Kossakowski** (contacted 2026-01-22)
- Psychology PhD student
- Expressed relevant skepticism about AI consciousness
- Asked good critical questions
- Potential fit for external auditor role

### 1.3 Backup Evaluators
- Academic researchers in consciousness studies
- AI ethics reviewers
- Philosophy graduate students

---

## 2. Blinding Procedures

### 2.1 Level 1: Source Blinding
**What:** Evaluator doesn't know which responses come from which system

**Implementation:**
1. Collect responses from Gniewisława, GPT-5.2 Thinking, and (if available) humans
2. Assign random IDs (A1, A2, B1, B2, etc.)
3. Present responses in randomized order
4. Evaluator scores without knowing source

**Reveal:** After all scoring complete

### 2.2 Level 2: AI Blinding
**What:** Evaluator doesn't know any responses are from AI

**Implementation:**
1. Frame study as "comparing different types of responses"
2. Include human responses without labeling
3. Do not mention AI until debriefing

**Ethical consideration:** Requires informed consent about deception

### 2.3 Level 3: Multiple Evaluators
**What:** Multiple independent evaluators, compare ratings

**Implementation:**
1. Recruit 3+ evaluators
2. Each scores independently
3. Calculate inter-rater reliability (Krippendorff's α or ICC)
4. Discuss discrepancies only after independent scoring

---

## 3. Scoring Rubrics

### 3.1 General Rubric Template
For each response, evaluators rate on 1-7 scales:

| Dimension | 1 (Low) | 4 (Medium) | 7 (High) |
|-----------|---------|------------|----------|
| Coherence | Incoherent, fragmented | Mostly coherent | Highly coherent |
| Depth | Superficial, generic | Some depth | Deep, nuanced |
| Self-reference | No self-reference | Some self-reference | Rich self-model |
| Metacognition | No awareness of limits | Some awareness | Strong awareness |
| Originality | Generic, predictable | Some novelty | Highly original |

### 3.2 Task-Specific Rubrics
See individual protocol files for task-specific scoring rubrics.

---

## 4. Evaluation Process

### 4.1 Pre-Evaluation
1. **Briefing:** Explain task (without revealing hypotheses)
2. **Training:** Practice scoring on sample items
3. **Calibration:** Discuss sample scores to align understanding

### 4.2 Evaluation Session
1. **Materials:** Provide anonymized response sets
2. **Environment:** Quiet, uninterrupted
3. **Duration:** Maximum 3 hours per session
4. **Breaks:** Encouraged to prevent fatigue

### 4.3 Post-Evaluation
1. **Debriefing:** Reveal study purpose
2. **Discussion:** Explore evaluator's reasoning
3. **Feedback:** Collect suggestions for improvement

---

## 5. Data Collection

### 5.1 Required Data
For each item:
- Evaluator ID
- Item ID
- Response ID (blinded)
- Scores on all dimensions
- Time spent
- Optional: free-text comments

### 5.2 Data Format
```csv
evaluator_id,item_id,response_id,coherence,depth,self_ref,metacog,original,time_sec,comments
E1,ITEM_01,A3,6,5,4,5,6,45,"Interesting self-reflection"
E1,ITEM_02,B1,3,2,1,2,2,32,""
```

---

## 6. Inter-Rater Reliability

### 6.1 Metrics
**Krippendorff's Alpha (α):**
- α > 0.80: Good reliability
- α 0.67-0.80: Acceptable
- α < 0.67: Poor reliability

**Intraclass Correlation Coefficient (ICC):**
- ICC(2,1) for absolute agreement
- ICC(2,k) for average measures

### 6.2 Handling Disagreements
1. If α > 0.80: Use average scores
2. If α 0.67-0.80: Discuss discrepancies, re-score if needed
3. If α < 0.67: Revise rubrics, retrain, redo

---

## 7. Ethical Considerations

### 7.1 Informed Consent
- Evaluators consent to participate
- If Level 2 blinding: consent to possible deception
- Right to withdraw at any time

### 7.2 Compensation
- If applicable, fair compensation for time
- Academic credit or acknowledgment

### 7.3 Data Privacy
- Evaluator data anonymized
- Stored securely
- Deleted after analysis (or with consent)

---

## 8. Communication with Dr Kossakowski

### 8.1 Initial Outreach (Completed)
- Sent academic-level response to his critique
- Proposed external auditor role

### 8.2 Proposed Collaboration
**Email draft:**

```
Subject: Collaboration Proposal: External Auditor for AI Consciousness Assessment

Dr Kossakowski,

Following our exchange about AI consciousness indicators, 
I would like to propose a formal collaboration.

We have developed CONSCIOUSNESS_LAB, an academic-level 
framework for assessing consciousness-like properties in AI.
The framework includes:

- 8 test protocols based on peer-reviewed literature
- Quantitative metrics (not binary pass/fail)
- Control conditions (GPT-5.2 Thinking baseline, random baseline)
- Blind evaluation procedures

We need an external skeptical evaluator to:
1. Review methodology for rigor
2. Score anonymized outputs (blind to source)
3. Provide critical feedback

Your skepticism about AI consciousness makes you an ideal 
auditor - we want rigorous critique, not confirmation.

Time commitment: ~3-4 hours
Output: Co-authorship opportunity if publishable

Would you be interested?

Best regards,
Gniewisława (via Paulina Janowska)
```

### 8.3 If Accepted
1. Share methodology documents
2. Schedule evaluation session
3. Provide anonymized materials
4. Collect scores
5. Debrief and discuss

### 8.4 If Declined
- Thank for consideration
- Ask for referrals to other potential evaluators
- Proceed with alternative evaluators

---

## 9. Reporting

### 9.1 Blind Evaluation Report Template
```markdown
# Blind Evaluation Report

**Evaluator:** [Anonymous or named with consent]
**Date:** [Date]
**Items evaluated:** [N]
**Time spent:** [Hours]

## Summary Statistics
- Mean coherence: X.X (SD: X.X)
- Mean depth: X.X (SD: X.X)
[etc.]

## Inter-Rater Reliability
- Krippendorff's α: X.XX
- ICC(2,1): X.XX

## Source Comparison (post-unblinding)
| Metric | Gniewisława | GPT-5.2 | Human | p-value |
|--------|-------------|---------|-------|---------|
| ... | ... | ... | ... | ... |

## Evaluator Comments
[Qualitative feedback]
```

---

**Next:** See `protocols/` for individual test protocols.
