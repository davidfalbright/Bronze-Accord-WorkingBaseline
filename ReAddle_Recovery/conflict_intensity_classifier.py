# conflict_intensity_classifier.py

from framework_models import ConflictAlert, ClassifiedConflict

class ConflictIntensityClassifier:
    def __init__(self, conviction_weights: dict):
        """
        conviction_weights: dict of {conviction_id: strength (1–100)}
        """
        self.conviction_weights = conviction_weights

    def classify(self, conflict: ConflictAlert) -> ClassifiedConflict:
        """
        Returns a ClassifiedConflict object based on severity, override rules, and resistance levels.
        """
        severity = conflict.severity
        override_type = self._determine_override_type(conflict)
        resistance_score = self._calculate_resistance(conflict)

        return ClassifiedConflict(
            source_1=conflict.source_1,
            source_2=conflict.source_2,
            override_type=override_type,
            severity=severity,
            resistance_score=resistance_score,
            description=conflict.description
        )

    def _determine_override_type(self, conflict: ConflictAlert):
        """
        Determine if one element should override the other based on known hierarchy.
        """
        if conflict.type == "Conviction over Principle":
            return "conviction_precedence"
        elif conflict.type == "Principle vs Safeguard":
            return "situation_dependent"
        else:
            return "unspecified"

    def _calculate_resistance(self, conflict: ConflictAlert):
        """
        Derives a 'resistance_score' (0–100) estimating how difficult it would be to override
        the protected element in context, weighted by conviction strength.
        """
        base = 30 if conflict.severity == "low" else 60 if conflict.severity == "moderate" else 85
        modifier = self.conviction_weights.get(conflict.source_1, 0) - self.conviction_weights.get(conflict.source_2, 0)
        return max(0, min(100, base + modifier))
