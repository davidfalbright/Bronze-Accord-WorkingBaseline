# How the System Works

## Overview

This system is **not** a replacement for powerful frontier LLMs (ChatGPT, Claude, DeepSeek, etc.). It is an **orchestration layer** that:

- **assesses** user input (including *optional* cognitive-style hypotheses such as MBTI, and *coarse* emotional tone),
- **compiles** a governed, attuned prompt for the frontier model (without injecting conclusions),
- **audits** the frontier model’s response for epistemic integrity and rhetorical/cognitive hazards.

The primary objective is to **offload heavy cognition to the frontier LLM** while enforcing **Interpretive Humility** and **epistemic discipline** end-to-end.

---

## Core Principles

1. **Interpretive Humility**
   - Interpretations are *hypotheses* with confidence bounds, not diagnoses or facts.
   - Confidence must scale with evidence.
   - Uncertainty is disclosed explicitly.

2. **Separation of Concerns**
   - Input assessment, prompt compilation, and output auditing are distinct functions.
   - No single function is allowed to both *interpret* and *assert authority*.

3. **LLM-Centric Reasoning**
   - The user’s chosen frontier LLM performs the main reasoning.
   - Local components do routing, constraint injection, caching, and lightweight lint/audit.

4. **Model-Agnostic Robustness**
   - Frontier model identity is treated as a claim unless corroborated.
   - If identity signals conflict, the system defaults to **UNKNOWN** and tightens constraints.

---

## Pipeline at a Glance

```
clean_data_contract_v1_1.yaml
        ↓
Input Assessor (right-brain analysis, multi-stream aware)
        ↓
Prompt Compiler (left-brain logic + epistemology)
        ↓
Counterparty Interface Coordinator
        ↓
Interaction Plan
        ↓
Frontier LLM / Robot / Device / Animal / Human
        ↓
Output Assessor (same lenses as input)
        ↓
Final Response
```

A global epistemology governor constrains the pipeline before and after generation.

---

## Epistemology Governor (Global)

### Files
- `root_epistemology_pre.yaml` — governs **how** reasoning is performed (pre / in-flight).
- `root_epistemology_post.yaml` — audits **what** was produced (post).

### What it governs
- Evidence hierarchy (established / provisional / speculative)
- Confidence discipline and uncertainty disclosure
- Verification triggers for online/retrieved information
- Hard bans on fabrication (citations, sources, quotes)

---

## (1) Input Assessor

### Purpose
Analyze **user input + conversation context** and emit *tags and hypotheses* that guide how the frontier model should think.

### What it assesses
- **Logical fallacy signals** (non-accusatory)
- **Cognitive bias signals** (non-accusatory)
- **Moral inversion risk**
- **Conversation drift / sudden goal shifts**
- **Emotional tone (coarse, probabilistic)**  
  Examples: calm / frustrated / anxious / excited / uncertain, with confidence bounds.
- **Communication-style hypothesis (optional)**  
  Examples: structured/direct preference; *optional* MBTI-style hypothesis with `user_confirmed=false` unless explicitly confirmed.

### Guardrails (Interpretive Humility)
- Emotional/MBTI outputs are **hypotheses**, not diagnoses.
- Tags are **signals**, not verdicts.
- The assessor does not decide truth and does not rewrite the user’s request.

---

## (2) Prompt Compiler

### Purpose
Transform the user’s request into a **frontier-LLM-ready prompt** that:
- preserves semantic intent,
- injects epistemic constraints,
- applies user attunement,
- applies model-attunement (instruction style tuning per frontier model).

### Inputs
- Raw user message
- `input_assessment` tags/hypotheses
- Epistemology governor (pre)
- Domain beliefs (left-brain logic/ethics)
- Frontier model profile (known or UNKNOWN)

### Output
- System/developer instruction blocks
- Normalized user ask
- Required output schema
- Optional verification plan request

---

## (3) Output Assessor

### Purpose
Audit the frontier model response for:
- epistemic integrity (uncertainty, evidence labeling, verification),
- fabrication bans,
- rhetorical/cognitive hazards using the **same taxonomy** used for user input.

### Checks
- fabricated citations/quotes/sources (hard block)
- overconfidence without evidence
- fallacies/bias patterns in model output
- moral inversion introduced by the model
- emotional escalation / manipulation
- drift from the user’s actual question
- overreach: stating emotional/MBTI inferences as facts

### Outcomes
- accept
- patch (targeted regeneration)
- ask clarifying question
- regen (rare)

---

## Packaging Modes

### Standard Pack (99% of customers)
- Prebuilt runtime bundles:
  - `bundle_pre_lite.yaml`
  - `bundle_pre_deep.yaml`
  - `bundle_post.yaml`
- One `bundle_manifest.yaml` describing exactly what is inside.

### Modular Compliance Pack (regulated clients)
- Ships discrete modules and a dependency graph:
  - `module_manifest.yaml`
  - optional `policy_provenance.yaml`

Both packaging modes compile to the same runtime contract and pipeline behavior.

---
