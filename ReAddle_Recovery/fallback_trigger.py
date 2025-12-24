# ===============================
# Module: fallback_trigger.py
# Purpose: Detect when braid's primary logic has failed or produced
#          no viable ethical verdict, and trigger fallback mode
# Part of: Fallback Exception System
# ===============================

import logging
from framework_models import EngineOutcome, FallbackTriggerDecision

logger = logging.getLogger(__name__)

def should_trigger_fallback(outcome: EngineOutcome) -> FallbackTriggerDecision:
    """
    Determine whether to initiate fallback logic due to failure or lack of output.

    Args:
        outcome (EngineOutcome): Result from the braid verdict engine.

    Returns:
        FallbackTriggerDecision: Decision with reason and trigger flag.
    """
    logger.debug("Evaluating fallback trigger conditions...")

    if not outcome.success:
        logger.warning("braid engine failed — triggering fallback.")
        return FallbackTriggerDecision(trigger=True, reason="Verdict engine failure")

    if outcome.verdict is None:
        logger.warning("No verdict returned — triggering fallback.")
        return FallbackTriggerDecision(trigger=True, reason="No verdict generated")

    if outcome.verdict.decision.lower() in ["unknown", "undetermined"]:
        logger.info("Uncertain verdict — fallback may be appropriate.")
        return FallbackTriggerDecision(trigger=True, reason="Verdict inconclusive")

    return FallbackTriggerDecision(trigger=False, reason="Primary logic succeeded")
