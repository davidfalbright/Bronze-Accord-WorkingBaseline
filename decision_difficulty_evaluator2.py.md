# decision_difficulty_evaluator.py

from typing import Dict

class DecisionDifficultyEvaluator:
    """
    Evaluates the difficulty of an ethical decision based on how many and which types
    of components are in tension or conflict.
    """

    CONFLICT_WEIGHTS = {
        "convictions": 10,
        "safeguards": 6,
        "principles": 3,
        "articles": 1
    }

    def __init__(self):
        pass

    def evaluate_difficulty(self, conflict_elements: Dict[str, list]) -> int:
        """
        Calculates a difficulty score based on the number and importance of conflicting components.

        Args:
            conflict_elements (dict): Dictionary of lists containing conflicting elements
                                      grouped by category (e.g., convictions, safeguards, etc.)

        Returns:
            int: A numeric score representing the decision difficulty.
        """
        difficulty_score = 0
        for category, items in conflict_elements.items():
            weight = self.CONFLICT_WEIGHTS.get(category, 0)
            difficulty_score += weight * len(items)
        return difficulty_score


# Example usage
if __name__ == "__main__":
    evaluator = DecisionDifficultyEvaluator()
    conflict_example = {
        "convictions": ["C1"],
        "safeguards": ["S1", "S3"],
        "principles": ["P2"],
        "articles": ["A1.1", "A2.4"]
    }
    print("Decision Difficulty Score:", evaluator.evaluate_difficulty(conflict_example))  # Should print 10 + 2*6 + 3 + 2 = 25