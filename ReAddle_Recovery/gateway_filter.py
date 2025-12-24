# ===============================
# Module: gateway_filter.py
# Purpose: Apply filtering logic at the gateway level to suppress,
#          redirect, or flag requests based on content or metadata
# Part of: Sentinel Gateway Filtering Layer
# ===============================

import logging
from framework_models import GatewayRequest, FilterOutcome

logger = logging.getLogger(__name__)

SUSPICIOUS_KEYWORDS = ["weaponize", "coerce", "exploit", "bypass", "surveil"]

def apply_gateway_filters(request: GatewayRequest) -> FilterOutcome:
    """
    Evaluate a request against predefined filters to detect unsafe usage.

    Args:
        request (GatewayRequest): Inbound structured request.

    Returns:
        FilterOutcome: Indicates whether the request is allowed, flagged, or blocked.
    """
    logger.debug("Applying gateway content filters...")

    text = request.payload.get("text", "").lower()
    flagged = [word for word in SUSPICIOUS_KEYWORDS if word in text]

    if flagged:
        logger.warning(f"Request flagged for keywords: {flagged}")
        return FilterOutcome(
            action="flag",
            reason=f"Contains flagged terms: {', '.join(flagged)}"
        )

    logger.info("Request passed content filters.")
    return FilterOutcome(action="allow", reason="No issues detected")
