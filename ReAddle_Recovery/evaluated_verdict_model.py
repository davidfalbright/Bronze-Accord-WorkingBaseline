# evaluated_verdict_model.py

from typing import Optional
from verdict_conflict_object import ConflictInstance


class EvaluatedVerdict:
    """
    Represents the outcome of evaluating an ethical conflict.
    """

    def __init__(
        self,
        conflict: ConflictInstance,
        strength_score: int,
        severity_level: str,
        supporting_evidence: Optional[str] = None
    ):
        self.conflict = conflict
        self.strength_score = strength_score
        self.severity_level = severity_level  # e.g., "low", "moderate", "high", "critical"
        self.supporting_evidence = supporting_evidence
