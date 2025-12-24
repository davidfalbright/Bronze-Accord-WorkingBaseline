# urgency_level_estimator.py

from typing import Dict


class UrgencyLevelEstimator:
    """
    Determines how urgently a proposed action must be taken or stopped.
    Uses severity, reversibility, and proximity to harm or ethical boundary.
    """

    def __init__(self):
        self.max_urgency = 1.0

    def estimate_urgency(
        self,
        harm_probability: float,
        time_to_impact_seconds: float,
        reversibility_score: float,
        stakeholder_exposure: int
    ) -> float:
        """
        Computes an urgency score.

        Args:
            harm_probability (float): Estimated chance of ethical harm (0.0–1.0).
            time_to_impact_seconds (float): Time before effect manifests.
            reversibility_score (float): How reversible the harm would be (0.0–1.0).
            stakeholder_exposure (int): Number of affected parties.

        Returns:
            float: Urgency score (0.0–1.0)
        """
        if harm_probability <= 0.0 or stakeholder_exposure == 0:
            return 0.0

        time_penalty = 1.0 if time_to_impact_seconds <= 1 else 1 / (1 + time_to_impact_seconds / 10)
        urgency = harm_probability * time_penalty * (1 - reversibility_score) * min(1.0, stakeholder_exposure / 100.0)

        return round(min(self.max_urgency, max(0.0, urgency)), 4)
