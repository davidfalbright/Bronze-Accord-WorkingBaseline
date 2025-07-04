# ===============================
# Module: fallback_override.py
# Purpose: Allow external override of fallback verdicts under
#          human review or external policy constraints
# Part of: Fallback Escalation & Review Layer
# ===============================

import logging
from framework_models import Verdict, OverrideRequest, OverrideResult

logger = logging.getLogger(__name__)

ALLOWED_OVERRIDES = {
    "emergency_human_command": "Override permitted by authorized reviewer",
    "policy_directive": "Override permitted by predefined policy route"
}

def attempt_override(verdict: Verdict, request: OverrideRequest) -> OverrideResult:
    """
    Attempt to override a fallback verdict based on an external input.

    Args:
        verdict (Verdict): The fallback verdict to potentially override.
        request (OverrideRequest): Contains justification and override source.

    Returns:
        OverrideResult: Outcome showing whether override succeeded.
    """
    logger.debug(f"Attempting override from source: {request.source}")

    if request.source in ALLOWED_OVERRIDES:
        logger.info(f"Override authorized: {request.source}")
        overridden_verdict = Verdict(
            decision=request.override_decision,
            strength="external",
            rationale=ALLOWED_OVERRIDES[request.source]
        )
        return OverrideResult(success=True, verdict=overridden_verdict)

    logger.warning("Override request denied.")
    return OverrideResult(success=False, verdict=verdict)