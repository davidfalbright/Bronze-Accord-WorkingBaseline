# Deep Research Protocol

The Deep Research Protocol defines the steps that must be followed when the assistant is asked to perform sustained or context-aware research within the Bronze Accord project.

---

## 🎯 Purpose

To ensure that:
- All research is archived
- All insights are traceable
- Memory losses do not compromise continuity
- Files are usable across environment resets

---

## 📋 Steps

1. **Receive a Research Request**
   - Ensure the user specifies the research focus
   - Interpret ambiguous terms using context

2. **Create Research Log**
   - Name: `Deep_Research_Log_YYYY-MM-DD_HHMM.md`
   - Record: query, date, summary of findings, and sources
   - Format for long-term clarity

3. **Archive the Research Log**
   - Run `run_archive_protocol()` on the log
   - Confirm footer elements and content integrity
   - Insert into ZIP archive

4. **Prompt for Memory Save**
   - Ask: “Would you like me to save this insight to memory?”
   - Respect user choice; if yes:
     - Create a corresponding memory backup file
     - Insert into archive (machine-readable if needed)

5. **Offer Summary or Next Action**
   - Provide brief actionable insight
   - Invite follow-up or handoff to another protocol

---

## 🧠 Notes

- Research logs are stored permanently unless overridden
- Memory file backups protect against workspace resets
- YAML block summaries may be used for machine parsing

---

Saved and finalized on: 2025-06-27 14:12  
David F. Albright, Architect of The Bronze Accord  
Creative Commons Attribution 4.0 (CC BY 4.0)
