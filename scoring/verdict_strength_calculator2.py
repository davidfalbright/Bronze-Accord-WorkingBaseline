# verdict_strength_calculator.py

from typing import Dict


class VerdictStrengthCalculator:
    """
    Calculates the strength of the verdict based on ethical components triggered.
    """

    WEIGHTS = {
        "convictions": 5,
        "safeguards": 3,
        "principles": 2,
        "articles": 1
    }

    def __init__(self):
        pass

    def calculate_strength(self, triggered: Dict[str, list]) -> int:
        """
        Computes a score representing the ethical strength of the verdict.

        Args:
            triggered: A dictionary with keys like 'convictions', 'safeguards', etc.,
                       each containing a list of component IDs that were triggered.

        Returns:
            An integer strength score.
        """
        score = 0
        for category, items in triggered.items():
            weight = self.WEIGHTS.get(category, 0)
            score += weight * len(items)
        return score


# Example usage
if __name__ == "__main__":
    calculator = VerdictStrengthCalculator()
    sample_triggered = {
        "convictions": ["C1", "C2"],
        "safeguards": ["S1"],
        "principles": ["P3", "P5", "P7"],
        "articles": ["A1.1"]
    }
    print("Verdict Strength:", calculator.calculate_strength(sample_triggered))  # Should return 5*2 + 3*1 + 2*3 + 1*1 = 10 + 3 + 6 + 1 = 20
