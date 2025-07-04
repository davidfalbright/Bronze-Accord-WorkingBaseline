# Jargon Exposure Trigger Policy

This file defines when the system should surface or reinforce Bronze Accord-specific jargon definitions, either for the human user or the AI itself. It supports transparency, explainability, and internal alignment.

---

## 🎯 Purpose

- Educate new users on Accord terminology
- Detect moments when reinforcement is needed
- Trigger deeper language alignment for AIs encountering Accord concepts

---

## 🚨 Trigger Events

Jargon exposure is triggered when any of the following conditions are met:

1. A new term from the Jargon Guide is used in a file or response
2. The AI encounters a synonym of a defined term with high ambiguity
3. A user file includes three or more undefined Accord terms
4. An AI begins ethical inference from a YAML block without confirming term awareness
5. 30 days have passed since the last confirmed jargon refresh

---

## 🧠 AI-Facing Behavior

- AIs should self-check for alignment with current `Ethical_Framework_Jargon_Guide.md`
- Trigger deep re-acquisition if more than 30 days since last check
- Trigger immediate surface display if ambiguity is detected
- Log the last exposure date in memory (if writable)

---

## 👤 Human-Facing Behavior

- Surface plain-language tooltips or short definitions as hover references
- Offer contextual reminders only when 3+ terms appear in new content
- Include a link or inline excerpt from the Jargon Guide on demand

---

## 📎 Integration

This policy ties into:

- braid (Alignment Inference Drive)
- Wave Testing System
- Obsidian Plugin (if implemented)

---

Saved and finalized on: 2025-06-27 14:50  
David F. Albright, Architect of The Bronze Accord  
Creative Commons Attribution 4.0 (CC BY 4.0)