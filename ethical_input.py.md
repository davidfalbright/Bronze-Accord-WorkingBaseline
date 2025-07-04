# ===============================
# Module: ethical_input.py
# Purpose: Define the structure for incoming user ethical queries
#          submitted to the system
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class EthicalInput:
    """
    Raw input submitted by the user for ethical evaluation.
    """
    text: str
    metadata: Optional[Dict[str, str]] = None