# braid_core.py.md

```python
# ===============================
# Module: braid_core.py
# Purpose: Define and initialize core logic functions that underpin
#          braid decision-making, confidence scoring, and layer traversal
# Part of: braid Core Engine
# ===============================

import logging
from framework_models import CoreInitializationResult, EthicsLayerConfig

logger = logging.getLogger(__name__)

CORE_STATE = {
    "initialized": False,
    "layer_config": None
}

def initialize_core_logic() -> bool:
    """
    Set up core logic structures and layer evaluation configuration.

    Returns:
        bool: True if successful, False otherwise.
    """
    logger.debug("Initializing braid core logic...")
    try:
        CORE_STATE["layer_config"] = EthicsLayerConfig.load_default()
        CORE_STATE["initialized"] = True
        logger.info("Core logic initialized with default layer config.")
        return True
    except Exception as e:
        logger.exception("Failed to initialize braid core logic.")
        return False

def is_core_ready() -> bool:
    """
    Check if the braid core has been successfully initialized.

    Returns:
        bool: Initialization state.
    """
    return CORE_STATE["initialized"]