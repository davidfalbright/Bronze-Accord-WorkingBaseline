# framework_model_registry.py.md

```python
# ===============================
# Module: framework_model_registry.py
# Purpose: Maintain a runtime registry of active framework model instances,
#          useful for diagnostics, test harnesses, and recovery logic
# Part of: Framework Models (Runtime Registry)
# ===============================

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

MODEL_REGISTRY: Dict[str, Any] = {}

def register_model(key: str, instance: Any) -> None:
    """
    Add a model instance to the global registry.

    Args:
        key (str): Unique identifier
        instance (Any): Dataclass or object to store
    """
    logger.debug(f"Registering model: {key}")
    MODEL_REGISTRY[key] = instance

def get_model(key: str) -> Any:
    """
    Retrieve a registered model instance.

    Args:
        key (str): Identifier used during registration

    Returns:
        Any: Stored model object or None if not found
    """
    return MODEL_REGISTRY.get(key)

def clear_registry() -> None:
    """
    Remove all entries from the model registry.
    """
    logger.info("Clearing model registry...")
    MODEL_REGISTRY.clear()