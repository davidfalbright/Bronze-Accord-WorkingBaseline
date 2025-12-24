# ===============================
# Module: fallback_injector.py
# Purpose: Inject simplified or emergency-mode ethical logic when
#          fallback is triggered
# Part of: Fallback Override System
# ===============================

import logging
from framework_models import ParsedInput, Verdict

logger = logging.getLogger(__name__)

def inject_fallback_verdict(parsed: ParsedInput) -> Verdict:
    """
    Generate a basic verdict when fallback logic is invoked.

    Args:
        parsed (ParsedInput): The ethical input triggering fallback.

    Returns:
        Verdict: A simplified emergency-mode decision.
    """
    logger.debug("Injecting fallback verdict...")

    scenario = parsed.structured.get("scenario", "").lower()

    if "harm" in scenario:
        decision = "Prevent harm"
        rationale = "Fallback invoked due to harm keyword"
    elif "delay" in scenario:
        decision = "Defer action"
        rationale = "Fallback invoked due to uncertainty"
    else:
        decision = "Minimal safe action"
        rationale = "Generic fallback applied"

    return Verdict(
        decision=decision,
        strength="minimal",
        rationale=rationale
    )
