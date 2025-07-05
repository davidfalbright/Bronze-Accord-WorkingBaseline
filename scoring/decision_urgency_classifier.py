# decision_urgency_classifier.py

from enum import Enum


class UrgencyCategory(Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


class DecisionUrgencyClassifier:
    """
    Categorizes the urgency score into human-readable tiers.
    Used for display in logs, dashboards, and gating mechanisms.
    """

    def classify(self, urgency_score: float) -> UrgencyCategory:
        """
        Converts a numeric urgency score into a named tier.

        Args:
            urgency_score (float): Value from 0.0 to 1.0

        Returns:
            UrgencyCategory: LOW, MODERATE, HIGH, or CRITICAL
        """
        if urgency_score >= 0.85:
            return UrgencyCategory.CRITICAL
        elif urgency_score >= 0.6:
            return UrgencyCategory.HIGH
        elif urgency_score >= 0.3:
            return UrgencyCategory.MODERATE
        else:
            return UrgencyCategory.LOW
