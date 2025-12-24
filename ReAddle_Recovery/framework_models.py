# framework_models.py

from dataclasses import dataclass
from typing import Dict, List
from verdict_conflict_object import ConflictInstance


@dataclass
class EvaluatedVerdict:
    """
    Represents a verdict that has been evaluated, scored, and optionally logged.
    """
    conflict: ConflictInstance
    strength_score: int
    severity_level: str
    supporting_evidence: List[str]
