# ===============================
# Module: yaml_intent_expander.py
# Purpose: Expand YAML enforcement items to include formalized
#          intent blocks for all ethical layers
# Part of: YAML Semantic Augmentation
# ===============================

import logging
from framework_models import YAMLExpansionRequest, YAMLExpansionResult

logger = logging.getLogger(__name__)

INTENT_TEMPLATES = {
    "conviction": "This conviction represents an unbreakable ethical stance focused on {subject}.",
    "safeguard": "This safeguard exists to prevent {threat} under all circumstances.",
    "principle": "This principle guides actions that promote {value}.",
    "article": "This article ensures that {outcome} is consistently upheld."
}

def expand_yaml_intents(request: YAMLExpansionRequest) -> YAMLExpansionResult:
    """
    Apply standard intent logic to YAML items lacking full intent text.

    Args:
        request (YAMLExpansionRequest): Items needing expansion.

    Returns:
        YAMLExpansionResult: Success state and expanded text blocks.
    """
    logger.debug("Expanding intents in YAML block...")
    expanded = {}

    try:
        for item_id, item_data in request.items.items():
            layer_type = item_data.get("type")
            key_term = item_data.get("keyword", "the protected value")

            template = INTENT_TEMPLATES.get(layer_type)
            if template:
                expanded[item_id] = template.format(
                    subject=key_term, threat=key_term, value=key_term, outcome=key_term
                )
            else:
                expanded[item_id] = f"Intent for {item_id} could not be expanded (unknown type)."

        return YAMLExpansionResult(success=True, expanded_intents=expanded)

    except Exception as e:
        logger.exception("Intent expansion failed.")
        return YAMLExpansionResult(success=False, expanded_intents={}, error=str(e))