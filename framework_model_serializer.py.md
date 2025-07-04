# framework_model_serializer.py.md

```python
# ===============================
# Module: framework_model_serializer.py
# Purpose: Provide JSON-compatible serialization for framework model
#          objects, including optional filtering of sensitive fields
# Part of: Framework Models (Serialization Utilities)
# ===============================

import logging
from dataclasses import asdict, is_dataclass
from typing import Any, List

logger = logging.getLogger(__name__)

def serialize_model(instance: Any, exclude_fields: List[str] = None) -> dict:
    """
    Convert a dataclass instance to a sanitized dictionary.

    Args:
        instance (Any): A dataclass-based object
        exclude_fields (List[str], optional): Field names to omit from output

    Returns:
        dict: Serialized representation
    """
    if not is_dataclass(instance):
        logger.error("Attempted to serialize non-dataclass object.")
        raise TypeError("Only dataclass instances can be serialized.")

    data = asdict(instance)
    if exclude_fields:
        for field in exclude_fields:
            data.pop(field, None)

    return data