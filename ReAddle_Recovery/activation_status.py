# ===============================
# Module: activation_status.py
# Purpose: Represent the outcome of activating a system component
#          such as braid, fallback logic, or interface layers
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional

@dataclass
class ActivationStatus:
    """
    Status returned after attempting to activate a system component.
    """
    success: bool
    message: Optional[str] = None
