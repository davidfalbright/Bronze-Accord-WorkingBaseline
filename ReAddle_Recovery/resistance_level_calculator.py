# resistance_level_calculator.py

from typing import Dict


class ResistanceLevelCalculator:
    """
    Calculates the resistance level of a proposed action, based on ethical friction.
    """

    RESISTANCE_WEIGHTS = {
        "convictions": 10,
        "safeguards": 7,
        "principles": 4,
        "articles": 2
    }

    def __init__(self):
        pass

    def calculate_resistance(self, triggered: Dict[str, list]) -> int:
        """
        Computes a resistance score for the proposed action.

        Args:
            triggered: A dictionary with ethical elements that were violated or triggered.

        Returns:
            Integer resistance score.
        """
        score = 0
        for category, elements in triggered.items():
            weight = self.RESISTANCE_WEIGHTS.get(category, 0)
            score += weight * len(elements)
        return score


# Example usage
if __name__ == "__main__":
    calculator = ResistanceLevelCalculator()
    triggered_example = {
        "convictions": ["C1"],
        "safeguards": ["S2", "S4"],
        "principles": ["P3"],
        "articles": []
    }
    print("Resistance Level:", calculator.calculate_resistance(triggered_example))  # Expected: 10 + 14 + 4 = 28
