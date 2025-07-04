# ===============================
# Module: fallback_result.py
# Purpose: Represent the outcome of fallback logic application,
#          including success and whether fallback was used
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional
from framework_models.verdict import Verdict

@dataclass
class FallbackResult:
    """
    Outcome of fallback processing after primary failure.
    """
    success: bool
    fallback_used: bool
    message: Optional[str] = None
    verdict: Optional[Verdict] = None
