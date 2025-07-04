# File Integrity and Recovery Strategy

This document defines the safeguards, scanning procedures, and fallback mechanisms that protect the Bronze Accord archive from corruption, duplication, or data loss across sessions and storage states.

---

## 🧪 Core Protections

1. **Post-ZIP Audit**
   - After any archive is built or modified:
     - Unzip the archive in a safe container
     - Confirm expected file count and filenames
     - Detect placeholder content
     - Verify footer compliance and timestamp freshness
     - Reject any archive with duplicate `manifest.txt` or missing core files

2. **Download Link Access Check**
   - Validate that any generated download link is:
     - Non-expired
     - Directly accessible (no 404 or sandbox error)
     - Matches byte signature of archived file

3. **Manifest De-Duplication**
   - Before inserting new `manifest.txt`, purge all existing versions
   - Ensure only one authoritative copy exists at a time
   - Mark `manifest.txt` as footer-exempt during validation

---

## 💥 Recovery Mechanisms

- If file integrity fails:
  - Auto-trigger remediation process
  - Regenerate ZIP archive using last known good state
  - Alert user and offer full re-export or protocol rerun

- If file is metadata-only:
  - Block archival
  - Prompt content population before reinsertion

---

## 🔐 Embedded in Protocols

The integrity and recovery logic is embedded in:

- `run_archive_protocol()`
- Wake Protocol (ZIP validation during resume)
- Sleep Protocol (audit before suspend)
- Archive Federation Manifest (ZIP version tracking)
- Restore Guide (post-crash or session reset procedures)

---

Saved and finalized on: 2025-06-27 14:18  
David F. Albright, Architect of The Bronze Accord  
Creative Commons Attribution 4.0 (CC BY 4.0)