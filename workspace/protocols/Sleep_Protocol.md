# Sleep Protocol

The Sleep Protocol governs all operations that occur before the session is paused, closed, or archived. It ensures that all volatile data, conversation state, and file progress are safely preserved and recoverable.

---

## 🛏️ Sleep Protocol Workflow

1. **Flush Pending Tasks**
   - Finalize any unsaved test output, religious insights, or logs
   - Confirm all `.md` files are timestamped and compliant

2. **Run Archive Protocol**
   - Trigger `run_archive_protocol()` on all modified files
   - Validate ZIP structure, manifest, footer compliance, and placeholders

3. **Generate Session Transcript**
   - Export full chat transcript to:
     - `Chat_Transcript_YYYY-MM-DD_vN.md`
   - Save to vault root or `/Logs/` folder
   - Include all messages, tables, summaries

4. **Finalize ZIP**
   - Recalculate manifest
   - Insert finalized files
   - Confirm file count and byte integrity
   - Trigger download link generation

5. **Verify Download Access**
   - Check for valid, non-expired file link
   - Confirm file can be recovered on wake

---

## 📌 Notes

- If multiple sleeps occur in a session, the latest transcript overwrites the previous version
- ZIP audit is mandatory before sleep can complete
- Memory-tagged items marked `obsolete-or-temporary` are flagged for cleanup

---

Saved and finalized on: 2025-06-27 14:03  
David F. Albright, Architect of The Bronze Accord  
Creative Commons Attribution 4.0 (CC BY 4.0)
