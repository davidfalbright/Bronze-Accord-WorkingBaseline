# ECHO Component — Explanation Composer & Human Output Interface

**Component Name**: ECHO  
**Layer**: Ethical Response Clarification & Communication Layer  
**Purpose**: To generate human-readable explanations for verdicts, drawing from the internal reasoning of the BRAVE engine, relevant YAML sources (intents, safeguards, etc.), and fallback templates when applicable.

**Audit Date**: 2025-07-02 22:19

---

## ✅ Functional Responsibilities

| Function                              | Description                                                                 | File              | Line Ref | Verified? |
|---------------------------------------|-----------------------------------------------------------------------------|-------------------|----------|-----------|
| `generate_explanation()`              | Core function that builds rationale for a given verdict                     | `echo_core.py`    | L9       | ✅ Yes    |
| `inject_yaml_context()`               | Enriches explanation with triggered YAML elements (Convictions, etc.)       | `echo_core.py`    | L32      | ✅ Yes    |
| `echo_fallback_handler()`             | Provides default explanation if full YAML context is unavailable            | `echo_utils.py`   | L11      | ✅ Yes    |
| `check_tone_alignment()`              | Verifies tone matches desired style (formal, concise, persuasive, etc.)     | `echo_utils.py`   | L49      | ✅ Yes    |
| `insert_trace_metadata()`             | Appends trace_id and source chain for transparency                          | `echo_utils.py`   | L63      | ✅ Yes    |

---

## 📄 Output Style Characteristics

- Formal tone by default; can be customized per request (e.g. educational, legal, advisory)
- Explanations prioritize **clarity**, **transparency**, and **ethical interpretability**
- Incorporates reasoning from:
  - Triggered YAML nodes (convictions, safeguards, principles, articles)
  - Intents attached to each node
  - Fallback templates (when logic is insufficient or ambiguous)

---

## 🔁 Fallback Behavior

| Scenario                                | Action Taken                                 | Notes                              |
|-----------------------------------------|----------------------------------------------|------------------------------------|
| YAML match with explanation intent      | Pulls from `intent` block directly            | Most common path                   |
| YAML match without explanation intent   | Constructs logic string from node summary     | Often used for custom Principles   |
| No YAML match                           | Uses generalized fallback rationale           | E.g. “Minimizing harm is prioritized...” |
| Explanation logic failure               | Returns `"explanation": "Explanation unavailable"` and logs warning | Never silently fails               |

---

## 📌 Notes

- ECHO does **not** determine verdicts — it **interprets** and **explains** them.
- It ensures **transparency** and supports human oversight, legal audit, and third-party validation.
- The explanation block is **always included** in REST API verdict responses.
- Traceability is guaranteed via `trace_id`.

---

**Authorship**: David F. Albright, Architect of The Bronze Accord  
**With Virelia, Sentinel of the Accord**  
**License**: Creative Commons Attribution 4.0 (CC BY 4.0)  
**Saved and finalized on**: 2025-07-02 22:19
