# braid_validator.py.md

```python
# ===============================
# Module: braid_validator.py
# Purpose: Validate parsed ethical input for structural and logical
#          soundness before verdict processing in braid
# Part of: braid Validation Layer
# ===============================

import logging
from framework_models import ParsedInput, ValidationResult

logger = logging.getLogger(__name__)

def validate_parsed_input(parsed: ParsedInput) -> ValidationResult:
    """
    Run structural and semantic validation checks on parsed input.

    Args:
        parsed (ParsedInput): Structured ethical input from parser.

    Returns:
        ValidationResult: Success/failure with reason if applicable.
    """
    logger.debug("Validating parsed ethical input...")

    if not parsed or not parsed.structured:
        return ValidationResult(success=False, message="Parsed input missing or incomplete.")

    # Example structural validation
    if not isinstance(parsed.structured, dict):
        return ValidationResult(success=False, message="Structured input must be a dictionary.")

    # Add additional semantic checks here
    if "scenario" not in parsed.structured:
        return ValidationResult(success=False, message="Missing 'scenario' key in input.")

    logger.info("Parsed input passed validation.")
    return ValidationResult(success=True, message="Validation successful.")

def check_validator_integrity() -> bool:
    """
    Perform a self-check of validator readiness.

    Returns:
        bool: True if validator is healthy, False otherwise.
    """
    try:
        dummy = ParsedInput(structured={"scenario": "Dummy"})
        result = validate_parsed_input(dummy)
        return result.success
    except Exception as e:
        logger.error(f"Validator integrity check failed: {e}")
        return False