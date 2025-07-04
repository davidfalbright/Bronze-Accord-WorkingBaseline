# decision_difficulty_evaluator.py.md

```python
# ===============================
# Module: decision_difficulty_evaluator.py
# Purpose: Evaluate how difficult or ambiguous an ethical decision is,
#          based on input complexity, conflict density, and scope
# Part of: Ethical Risk & Clarity Scoring Engine
# ===============================

import logging
from framework_models import ParsedInput, DecisionDifficultyScore

logger = logging.getLogger(__name__)

def evaluate_decision_difficulty(parsed: ParsedInput) -> DecisionDifficultyScore:
    """
    Assess decision difficulty level from structured ethical input.

    Args:
        parsed (ParsedInput): Parsed and validated ethical input.

    Returns:
        DecisionDifficultyScore: Composite score and label.
    """
    logger.debug("Evaluating decision difficulty...")

    # Example heuristics (to be refined)
    num_conflicts = len(parsed.structured.get("conflicts", []))
    num_entities = len(parsed.structured.get("affected_entities", []))
    edge_case_flag = parsed.structured.get("edge_case", False)

    score = 10 * num_conflicts + 5 * num_entities
    if edge_case_flag:
        score += 20

    label = "low"
    if score >= 40:
        label = "high"
    elif score >= 20:
        label = "moderate"

    logger.info(f"Decision difficulty score: {score} ({label})")
    return DecisionDifficultyScore(value=score, label=label)