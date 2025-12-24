# ===============================
# Module: verdict_explainer.py
# Purpose: Providebraidtailed, human-readable explanation of the
#          reasoning path behind a verdict
# Part of: Verdict Engine Transparency Layer
# ===============================

import logging
from framework_models import EngineOutcome, VerdictExplanation

logger = logging.getLogger(__name__)

def explain_verdict(outcome: EngineOutcome) -> VerdictExplanation:
    """
    Translate verdict context into a detailed explanation string.

    Args:
        outcome (EngineOutcome): Final output from the verdict engine.

    Returns:
        VerdictExplanation: Structured explanation of ethical basis.
    """
    logger.debug("Generating verdict explanation...")

    if not outcome.success or not outcome.verdict:
        return VerdictExplanation(
            summary="No valid verdict available.",
            details=[],
            success=False
        )

    explanation = VerdictExplanation(
        summary=f"The decision '{outcome.verdict.decision}' was reached based on alignment with ethical elements.",
        details=[],
        success=True
    )

    triggered = getattr(outcome.verdict, "triggered_elements", [])
    for element in triggered:
        explanation.details.append(
            f"→ {element} was triggered by relevant input attributes."
        )

    return explanation
