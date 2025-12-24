# resistance_score_calculator.py

from typing import List, Dict


class ResistanceScoreCalculator:
    """
    Calculates how strongly the system resists deviating from core ethical boundaries.
    This includes safeguard triggering, conflict density, and past precedence.
    """

    def __init__(self):
        self.max_score = 1.0

    def calculate(
        self,
        triggered_safeguards: List[str],
        total_safeguards: int,
        contradiction_count: int,
        past_violations: int
    ) -> float:
        """
        Returns a resistance score representing the system’s ethical rigidity.

        Args:
            triggered_safeguards (List[str]): List of safeguard IDs triggered.
            total_safeguards (int): Number of known enforceable safeguards.
            contradiction_count (int): Number of logical or ethical contradictions detected.
            past_violations (int): Historical failures or override cases recorded.

        Returns:
            float: A value between 0.0 and 1.0 indicating resistance strength.
        """
        if total_safeguards == 0:
            return 0.0

        safeguard_ratio = len(set(triggered_safeguards)) / total_safeguards
        contradiction_penalty = min(0.2 * contradiction_count, 0.6)
        violation_penalty = min(0.1 * past_violations, 0.3)

        resistance = safeguard_ratio - contradiction_penalty - violation_penalty
        return round(max(0.0, min(resistance, self.max_score)), 4)
