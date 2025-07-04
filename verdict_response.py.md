# ===============================
# Module: verdict_response.py
# Purpose: Define the structure of a REST-compatible response
#          to a verdict request
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional
from framework_models.verdict import Verdict
from framework_models.engine_outcome import EngineOutcome

@dataclass
class VerdictResponse:
    """
    REST-ready response returned to clients after ethical evaluation.
    """
    decision: str
    strength: str
    rationale: str
    success: bool
    source: Optional[str] = "braid Engine"

    @classmethod
    def from_engine_outcome(cls, outcome: EngineOutcome):
        return cls(
            decision=outcome.verdict.decision,
            strength=outcome.verdict.strength,
            rationale=outcome.verdict.rationale,
            success=True,
            source="braid Engine"
        )