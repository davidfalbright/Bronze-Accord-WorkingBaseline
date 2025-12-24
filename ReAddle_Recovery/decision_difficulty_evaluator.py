# decision_difficulty_evaluator.py

from typing import Dict


class DecisionDifficultyEvaluator:
    """
    Evaluates how difficult a decision is based on ethical conflict intensity.
    """

    LAYER_WEIGHTS = {
        "convictions": 4.0,
        "safeguards": 3.0,
        "principles": 2.0,
        "articles": 1.0
    }

    def __init__(self):
        pass

    def evaluate_difficulty(self, triggered: Dict[str, list]) -> float:
        """
        Computes a normalized difficulty score from 0.0 to 1.0.

        Args:
            triggered: A dictionary of triggered ethical layers.

        Returns:
            A float indicating difficulty (0 = trivial, 1 = highly conflicted).
        """
        total_score = 0
        max_possible_score = 0

        for layer, violations in triggered.items():
            weight = self.LAYER_WEIGHTS.get(layer, 0)
            total_score += weight * len(violations)
            max_possible_score += weight * 5  # assume up to 5 per layer

        if max_possible_score == 0:
            return 0.0

        score = total_score / max_possible_score
        return min(round(score, 2), 1.0)


# Example usage
if __name__ == "__main__":
    evaluator = DecisionDifficultyEvaluator()
    sample_violations = {
        "convictions": ["C2"],
        "principles": ["P1", "P5", "P8"],
        "articles": ["A2.1", "A2.2"]
    }
    print("Decision Difficulty:", evaluator.evaluate_difficulty(sample_violations))  # Example output: 0.39
