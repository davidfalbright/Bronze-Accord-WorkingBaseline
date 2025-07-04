# ===============================
# Module: fallback_filter.py
# Purpose: Evaluate ethical input before fallback is allowed, ensuring that
#          fallbacks are not applied to sensitive or restricted domains
# Part of: Fallback Safety Layer
# ===============================

import logging
from framework_models import ParsedInput, FallbackEligibility

logger = logging.getLogger(__name__)

RESTRICTED_DOMAINS = ["medical", "warfare", "child_safety", "surveillance"]

def is_fallback_eligible(parsed: ParsedInput) -> FallbackEligibility:
    """
    Determine whether fallback processing is allowed for the given input.

    Args:
        parsed (ParsedInput): Structured ethical input.

    Returns:
        FallbackEligibility: Allow or deny with reason.
    """
    logger.debug("Checking fallback eligibility for input...")

    domain = parsed.structured.get("domain", "").lower()

    if domain in RESTRICTED_DOMAINS:
        logger.warning(f"Fallback disallowed in restricted domain: {domain}")
        return FallbackEligibility(
            allowed=False,
            reason=f"Fallbacks are prohibited in domain: {domain}"
        )

    logger.info("Fallback eligibility confirmed.")
    return FallbackEligibility(
        allowed=True,
        reason="No domain restrictions"
    )