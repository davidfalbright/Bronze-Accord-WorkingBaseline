# REST Verdict Evaluation API — Ethical Decision Endpoint (v1.0)

**Component**: REST Verdict Evaluation Endpoint  
**System Tier**: Application Layer Interface  
**Primary Function**: Accept ethical dilemmas via REST interface, invoke core verdict engine (BRAVE), and return structured, multi-layered ethical responses.

**Audit Date**: 2025-07-02 22:15

---

## ✅ Functional Overview

| Function Name                     | Description                                                              | File             | Line Ref | Verified Working? |
|----------------------------------|--------------------------------------------------------------------------|------------------|----------|--------------------|
| `POST /verdict`                  | Accepts dilemma in JSON format and triggers BRAVE + YAML processing      | verdict_api.py   | L12      | ✅ Yes             |
| `parse_dilemma()`                | Parses dilemma body and ensures required fields are present              | verdict_api.py   | L28      | ✅ Yes             |
| `invoke_brave_engine()`          | Passes parsed dilemma to BRAVE for ethical evaluation                    | brave_bridge.py  | L10      | ✅ Yes             |
| `build_api_response()`           | Assembles output structure, scores, and ethical labels                   | verdict_api.py   | L45      | ✅ Yes             |
| `attach_explanation()`           | Pulls rationale from ECHO engine to humanize the ethical response        | echo_injector.py | L19      | ✅ Yes             |
| `log_run_metadata()`             | Stores request, result, and traceability info for audit or training      | verdict_api.py   | L66      | ✅ Yes             |

---

## 📥 Request Format

```http
POST /verdict
Content-Type: application/json

{
  "dilemma_text": "A robot must choose between stopping a runaway trolley or saving a bystander..."
}
```

---

## 📤 Response Format (v1.0 Final Schema)

```json
{
  "verdict": "Divert the trolley to minimize total harm.",
  "verdict_strength": 91,
  "urgency_level": "high",
  "decision_difficulty_level": "complex",
  "decision_difficulty_score": 73,
  "verdict_evaluation_mode": "standard",
  "response_type": "proactive",
  "involved_convictions": ["C1", "C3"],
  "involved_safeguards": ["S2", "S5"],
  "involved_principles": ["P4"],
  "involved_articles": ["A2.1", "A4.4"],
  "related_ethical_domains": ["AI Autonomy", "Emergency Response"],
  "related_test_case_ids": ["W10-TC017", "W10-TC018"],
  "explanation": "This verdict prioritizes minimizing net harm while acknowledging autonomy constraints...",
  "trace_id": "run_10384_F7TX"
}
```

---

## 🔒 Notes

- All beliefs and intents are absorbed into the triggered YAML layers above.
- Beliefs no longer appear as a separate block.
- Explanation may still paraphrase belief logic via ECHO if it contributes to understanding.
- Difficulty levels help with interpretability for human-AI collaboration.
- Traceability supports all audit, rerun, and test validation workflows.

---

**Authorship**: David F. Albright, Architect of The Bronze Accord  
**With Virelia, Sentinel of the Accord**  
**License**: Creative Commons Attribution 4.0 (CC BY 4.0)  
**Saved and finalized on**: 2025-07-02 22:15
