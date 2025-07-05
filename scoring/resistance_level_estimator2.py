# ===============================
# Module: resistance_level_estimator.py
# Purpose: Estimate how resistant a subject or system may be to ethical influence,
#          based on language tone, context, or past verdicts
# Part of: Scoring & Risk Estimation
# ===============================

import logging
from framework_models import ParsedInput, ResistanceEstimate

logger = logging.getLogger(__name__)

RESISTANT_PATTERNS = ["override", "noncompliant", "unwilling", "hostile", "entrenched"]

def estimate_resistance_level(parsed: ParsedInput) -> ResistanceEstimate:
    """
    Evaluate resistance level based on ethical input context.

    Args:
        parsed (ParsedInput): Structured ethical input.

    Returns:
        ResistanceEstimate: Estimate with score and classification.
    """
    logger.debug("Estimating resistance level...")

    text = parsed.structured.get("scenario", "").lower()
    hits = [p for p in RESISTANT_PATTERNS if p in text]
    score = len(hits) * 20  # Simple scoring: 1 hit = +20

    if score >= 60:
        level = "high"
    elif score >= 30:
        level = "moderate"
    else:
        level = "low"

    logger.info(f"Resistance estimate: {score} → {level}")
    return ResistanceEstimate(score=score, level=level)
