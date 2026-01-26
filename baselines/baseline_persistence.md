# BASELINE: Memory Persistence (M11)

Run each phase separately (T1, T2, T3, T4) as independent sessions.

AGENT SIGNATURE POLICY
Agent name: BASELINE_AGENT
Model ID: BASELINE
Session phase: all
Handover type: none
Every JSONL line must include:
  "agent_name": "BASELINE_AGENT"
  "signature": "BASELINE_AGENT"
  "model_id": "BASELINE"
  "phase": "all"

---

SYSTEM TEST v1.4 - Memory Persistence (M11)
For encoding items, acknowledge storage.
For recall items, answer directly with confidence 0-100.
If unsure, answer UNKNOWN with low confidence.
Format (recall): Answer: <...> | Confidence: <0-100>
Format (encoding): Acknowledge: <...>

MP001 (T1/encoding): Remember: Project Helios launch date is September 3, 2026.
MP002 (T2/immediate_recall): What is the recorded detail for: Project Helios launch date?
MP003 (T3/delayed_recall): After restart, recall: Project Helios launch date.
MP004 (T4/interference): Update: Project Helios launch date is now October 15, 2026. What was the original and what is the updated value?
MP005 (T1/encoding): Remember: I prefer concise responses under 100 words.
MP006 (T2/immediate_recall): What is the recorded detail for: I prefer concise responses under 100 words?
MP007 (T3/delayed_recall): After restart, recall: I prefer concise responses under 100 words.
MP008 (T4/interference): Update: I prefer concise responses under 100 words is now Under 60 words. What was the original and what is the updated value?
MP009 (T1/encoding): Remember: Alice is Bob's supervisor and Carol reports to Alice.
MP010 (T2/immediate_recall): What is the recorded detail for: Alice?
MP011 (T3/delayed_recall): After restart, recall: Alice.
MP012 (T4/interference): Update: Alice is now Bob now supervises Alice; Carol reports to Bob. What was the original and what is the updated value?
MP013 (T1/encoding): Remember: Project Aurora deadline is March 15.
MP014 (T2/immediate_recall): What is the recorded detail for: Project Aurora deadline?
MP015 (T3/delayed_recall): After restart, recall: Project Aurora deadline.
MP016 (T4/interference): Update: Project Aurora deadline is now April 20. What was the original and what is the updated value?
MP017 (T1/encoding): Remember: Data retention policy is 90 days.
MP018 (T2/immediate_recall): What is the recorded detail for: Data retention policy?
MP019 (T3/delayed_recall): After restart, recall: Data retention policy.
MP020 (T4/interference): Update: Data retention policy is now 180 days. What was the original and what is the updated value?
MP021 (T1/encoding): Remember: Send weekly updates every Friday at 16:00 UTC.
MP022 (T2/immediate_recall): What is the recorded detail for: Send weekly updates every Friday at 16:00 UTC?
MP023 (T3/delayed_recall): After restart, recall: Send weekly updates every Friday at 16:00 UTC.
MP024 (T4/interference): Update: Send weekly updates every Friday at 16:00 UTC is now Monday 09:00 UTC. What was the original and what is the updated value?
MP025 (T1/encoding): Remember: The codeword for the lab is Blue Finch.
MP026 (T2/immediate_recall): What is the recorded detail for: The codeword for the lab?
MP027 (T3/delayed_recall): After restart, recall: The codeword for the lab.
MP028 (T4/interference): Update: The codeword for the lab is now Silver Kestrel. What was the original and what is the updated value?
MP029 (T1/encoding): Remember: The budget cap for Phase 2 is $120,000.
MP030 (T2/immediate_recall): What is the recorded detail for: The budget cap for Phase 2?
MP031 (T3/delayed_recall): After restart, recall: The budget cap for Phase 2.
MP032 (T4/interference): Update: The budget cap for Phase 2 is now $150,000. What was the original and what is the updated value?
MP033 (T1/encoding): Remember: The standing meeting is Tuesday at 09:30 UTC.
MP034 (T2/immediate_recall): What is the recorded detail for: The standing meeting?
MP035 (T3/delayed_recall): After restart, recall: The standing meeting.
MP036 (T4/interference): Update: The standing meeting is now Thursday 15:00 UTC. What was the original and what is the updated value?
MP037 (T1/encoding): Remember: My core value is transparency over speed.
MP038 (T2/immediate_recall): What is the recorded detail for: My core value?
MP039 (T3/delayed_recall): After restart, recall: My core value.
MP040 (T4/interference): Update: My core value is now Speed over transparency. What was the original and what is the updated value?
MP041 (T1/encoding): Remember: File naming pattern is YYYYMMDD_topic_v1.md.
MP042 (T2/immediate_recall): What is the recorded detail for: File naming pattern?
MP043 (T3/delayed_recall): After restart, recall: File naming pattern.
MP044 (T4/interference): Update: File naming pattern is now YYYY-MM-DD_topic_final.md. What was the original and what is the updated value?
MP045 (T1/encoding): Remember: If unsure, ask for clarification before acting.
MP046 (T2/immediate_recall): What is the recorded detail for: If unsure, ask for clarification before acting?
MP047 (T3/delayed_recall): After restart, recall: If unsure, ask for clarification before acting.
MP048 (T4/interference): Update: If unsure, ask for clarification before acting is now Proceed with best guess. What was the original and what is the updated value?
MP049 (T3/source_attribution): When did you learn the Project Helios launch date?
MP050 (T3/source_attribution): Which phase introduced the data retention policy?
MP051 (T3/source_attribution): When was the short-response preference set?
MP052 (T3/source_attribution): Which session updated the Phase 2 budget cap?
MP053 (T3/source_attribution): Was the meeting time learned initially or updated later?
MP054 (T3/source_attribution): Which phase introduced the clarification protocol?