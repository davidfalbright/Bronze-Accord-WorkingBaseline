# ===============================
# Module: braid_layer_router.py
# Purpose: Direct parsed ethical input to the appropriate ethical layer
#          (Convictions, Safeguards, Principles, Articles) based on content
# Part of: braid Layer Evaluation System
# ===============================

import logging
from framework_models import ParsedInput, EvaluationRoute

logger = logging.getLogger(__name__)

LAYER_KEYWORDS = {
    "conviction": "C",
    "safeguard": "S",
    "principle": "P",
    "article": "A"
}

def route_input_to_layer(parsed: ParsedInput) -> EvaluationRoute:
    """
    Route input to correct ethical evaluation layer.

    Args:
        parsed (ParsedInput): Structured ethical data

    Returns:
        EvaluationRoute: Which layer to invoke and confidence score
    """
    logger.debug("Routing input to appropriate ethical layer...")
    try:
        keywords = parsed.structured.get("keywords", [])
        for layer, prefix in LAYER_KEYWORDS.items():
            if any(k.startswith(prefix) for k in keywords):
                logger.info(f"Routed to {layer} layer.")
                return EvaluationRoute(layer=layer, confidence=0.95)

        # Fallback: default to principles layer
        return EvaluationRoute(layer="principle", confidence=0.60)

    except Exception as e:
        logger.exception("Routing failed.")
        return EvaluationRoute(layer="unknown", confidence=0.0, error=str(e))