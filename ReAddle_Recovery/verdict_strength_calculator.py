# verdict_strength_calculator.py

from framework_models import EvaluatedVerdict, ClassifiedConflict

class VerdictStrengthCalculator:
    def __init__(self, conviction_weights: dict):
        """
        conviction_weights: dict of {conviction_id: strength (1–100)}
        """
        self.conviction_weights = conviction_weights

    def calculate(self, conflict: ClassifiedConflict, evidence_count: int, severity: str) -> EvaluatedVerdict:
        """
        Returns an EvaluatedVerdict with a strength score (0–100) representing ethical confidence.
        """
        base = self._base_strength_from_evidence(evidence_count)
        conviction_modifier = self._modifier_from_convictions(conflict)
        severity_modifier = self._modifier_from_severity(severity)

        total_strength = base + conviction_modifier + severity_modifier
        total_strength = max(0, min(100, total_strength))

        return EvaluatedVerdict(
            conflict=conflict,
            strength_score=total_strength,
            supporting_evidence=evidence_count,
            severity_level=severity
        )

    def _base_strength_from_evidence(self, count: int) -> int:
        if count == 0:
            return 10
        elif count < 3:
            return 30
        elif count < 6:
            return 50
        else:
            return 70

    def _modifier_from_convictions(self, conflict: ClassifiedConflict) -> int:
        weight_1 = self.conviction_weights.get(conflict.source_1, 0)
        weight_2 = self.conviction_weights.get(conflict.source_2, 0)
        return (weight_1 - weight_2) // 4

    def _modifier_from_severity(self, severity: str) -> int:
        if severity == "low":
            return -5
        elif severity == "moderate":
            return 0
        elif severity == "high":
            return 10
        else:
            return 0
