# ===============================
# Module: parsed_input.py
# Purpose: Define the structured representation of ethical input
#          after braid parsing
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class ParsedInput:
    """
    Structured result of input parsing for ethical evaluation.
    """
    structured: Dict[str, Any]
    raw_text: str