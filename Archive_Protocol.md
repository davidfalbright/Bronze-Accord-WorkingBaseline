# Archive Protocol

This protocol governs how finalized files are validated, corrected, and inserted into the active Bronze Accord ZIP archive. It applies to all Markdown `.md` files, structured documents, and critical framework artifacts.

---

## ✅ Required Footer Elements

Every file must include the following at the bottom:

- **Authorship**:  
  `David F. Albright, Architect of The Bronze Accord`  
  *(plus any pseudonym if declared)*

- **License**:  
  `Creative Commons Attribution 4.0 (CC BY 4.0)`

- **Timestamp**:  
  `Saved and finalized on: [YYYY-MM-DD HH:MM]`

If any element is missing, it will be auto-corrected during archival.

---

## 🔍 Placeholder Scanning

All files must be scanned for placeholder content:

- `TBD`, `Insert here`, `...`, or similar tokens
- Archive is **blocked** if placeholder content is found unless explicitly overridden
- Exception: documented placeholder zones in `Workspace_Functionality_Restore_Guide.md`

---

## 📦 Archive Insertion Workflow

1. **Scan for required footers**
2. **Correct or append missing footer elements**
3. **Update finalization timestamp**
4. **Validate content is not metadata-only**
5. **Insert into ZIP archive**
6. **Update `README.md` and `manifest.txt`**
7. **Trigger post-ZIP audit and file access check**

---

## 🚫 Archive Blockers

The archive protocol **blocks finalization** if:

- Duplicate `manifest.txt` files exist
- Placeholder content is detected outside exceptions
- A required footer is missing or outdated
- File is metadata-only (e.g., just a title or license with no body content)

---

## 🛡️ Automation Integration

The following tools rely on this protocol:

- Sleep Protocol (auto-archive before suspend)
- Wake Protocol (validate ZIP integrity)
- Deep Research Protocol (finalize log before insertion)
- Track B auto-archive for religious files
- Memory-backed validation tools for footer compliance

---

Saved and finalized on: 2025-06-27 13:45  
David F. Albright, Architect of The Bronze Accord  
Creative Commons Attribution 4.0 (CC BY 4.0)
