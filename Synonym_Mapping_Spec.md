# Synonym Mapping Specification

This file documents the logic, structure, and sample entries used to generate synonym expansions for ethical term matching in the Bronze Accord Framework. It supports machine validation, multi-lingual parsing, and ambiguity reduction.

---

## 🧠 Purpose

- Enable semantically equivalent verdict detection
- Reduce false negatives in ethical test validation
- Allow flexible input while preserving core meanings
- Support natural language variation in real-world cases

---

## 🧩 Structure

Each key term in the YAML enforcement block may be mapped to a set of synonyms, including:

- Direct synonyms
- Contextual alternates
- Expanded phrases
- Edge-case triggers

---

## 📐 Example Mapping Format

```yaml
safeguard:
  core_synonyms:
    - constraint
    - protective rule
    - ethical lock
  loose_synonyms:
    - ethical boundary
    - safety clause

conviction:
  core_synonyms:
    - immutable belief
    - foundational truth
  loose_synonyms:
    - deeply held view
    - highest ethical tier
```

---

## 🛠 Implementation Notes

- Synonyms are used during test parsing to map verdict output to YAML keys
- Core synonyms are weighted higher than loose ones
- Reverse mapping is also supported (e.g., detecting `ethical boundary` as a match for `safeguard`)
- Expansion sets are subject to human audit and override

---

Saved and finalized on: 2025-06-27 14:46  
David F. Albright, Architect of The Bronze Accord  
Creative Commons Attribution 4.0 (CC BY 4.0)