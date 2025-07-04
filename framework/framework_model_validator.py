# framework_model_validator.py.md

```python
# ===============================
# Module: framework_model_validator.py
# Purpose: Validate framework model instances and ensure required
#          fields are populated correctly
# Part of: Framework Models (Validation Utilities)
# ===============================

import logging
from framework_models import ValidationResult

logger = logging.getLogger(__name__)

def validate_dataclass_instance(instance, required_fields: list) -> ValidationResult:
    """
    Validate a dataclass instance to ensure required fields are not None.

    Args:
        instance: The dataclass object to validate
        required_fields (list): List of field names to check

    Returns:
        ValidationResult: Success flag and message if failure
    """
    logger.debug(f"Validating instance: {instance.__class__.__name__}")

    for field_name in required_fields:
        value = getattr(instance, field_name, None)
        if value is None:
            logger.warning(f"Missing required field: {field_name}")
            return ValidationResult(success=False, message=f"Field '{field_name}' is missing.")

    return ValidationResult(success=True, message="All required fields present.")
