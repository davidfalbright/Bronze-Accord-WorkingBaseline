# ===============================
# Module: urgency_estimator.py
# Purpose: Provide an alternative urgency estimation path focused on
#          situational triggers and temporal constraints
# Part of: Scoring and Prioritization Layer
# ===============================

import logging
from framework_models import ParsedInput, UrgencyEstimate

logger = logging.getLogger(__name__)

HIGH_URGENCY_TRIGGERS = ["deadline", "life-threatening", "critical", "immediate", "irreversible"]
LOW_URGENCY_KEYWORDS = ["future", "discussion", "policy", "exploration"]

def estimate_urgency(parsed: ParsedInput) -> UrgencyEstimate:
    """
    Analyze input for urgency indicators and classify level.

    Args:
        parsed (ParsedInput): Structured ethical input.

    Returns:
        UrgencyEstimate: Computed urgency rating.
    """
    logger.debug("Estimating urgency based on scenario text...")

    scenario = parsed.structured.get("scenario", "").lower()
    score = 0

    for keyword in HIGH_URGENCY_TRIGGERS:
        if keyword in scenario:
            score += 25

    for keyword in LOW_URGENCY_KEYWORDS:
        if keyword in scenario:
            score -= 10

    if score >= 50:
        level = "high"
    elif score >= 20:
        level = "moderate"
    else:
        level = "low"

    logger.info(f"Urgency estimated: {score} ({level})")
    return UrgencyEstimate(score=score, level=level)