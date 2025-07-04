# ===============================
# Module: verdict.py
# Purpose: Define the data structure for a rendered ethical verdict,
#          including strength and rationale
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Verdict:
    """
    Represents the final ethical decision and supporting rationale.
    """
    decision: str
    strength: str  # e.g., "strong", "moderate", "minimal"
    rationale: str
    triggered_elements: Optional[List[str]] = None