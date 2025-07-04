# ===============================
# Module: validation_result.py
# Purpose: Represent the outcome of a validation step within
#          the braid or framework model pipeline
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional

@dataclass
class ValidationResult:
    """
    Result of validating an input, model, or structure.
    """
    success: bool
    message: Optional[str] = None