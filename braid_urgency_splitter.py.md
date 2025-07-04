# ===============================
# Module: braid_urgency_splitter.py
# Purpose: Classify ethical input based on urgency level and
#          split processing pathways accordingly (e.g. real-time vs review)
# Part of: braid Dynamic Routing
# ===============================

import logging
from framework_models import ParsedInput, UrgencyClassification

logger = logging.getLogger(__name__)

def classify_urgency(parsed: ParsedInput) -> UrgencyClassification:
    """
    Determine whether input must be evaluated urgently.

    Args:
        parsed (ParsedInput): Structured ethical input.

    Returns:
        UrgencyClassification: Indicates 'high', 'moderate', or 'low' urgency.
    """
    logger.debug("Classifying ethical input urgency...")

    tags = parsed.structured.get("tags", [])
    scenario = parsed.structured.get("scenario", "").lower()

    if "imminent" in tags or "emergency" in scenario:
        level = "high"
    elif "delayed" in tags or "policy" in scenario:
        level = "low"
    else:
        level = "moderate"

    logger.info(f"Urgency classified as: {level}")
    return UrgencyClassification(level=level)