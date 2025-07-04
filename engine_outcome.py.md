# ===============================
# Module: engine_outcome.py
# Purpose: Define the structure and status of a full verdict engine result,
#          including verdict, message, and success state
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional
from framework_models.verdict import Verdict

@dataclass
class EngineOutcome:
    """
    Full output from the verdict engine after processing input.
    """
    success: bool
    verdict: Optional[Verdict] = None
    message: Optional[str] = None