# resistance_level_estimator.py

from typing import Dict


class ResistanceLevelEstimator:
    """
    Estimates the resistance level based on ethical violations.
    """

    BASE_RESISTANCE = {
        "convictions": 90,
        "safeguards": 60,
        "principles": 30,
        "articles": 10
    }

    def __init__(self):
        pass

    def estimate_resistance(self, triggered: Dict[str, list]) -> int:
        """
        Calculates the resistance level to an action based on triggered violations.

        Args:
            triggered: A dictionary of triggered ethical elements.

        Returns:
            An integer from 0 to 100 representing resistance level.
        """
        total = 0
        count = 0

        for layer, items in triggered.items():
            weight = self.BASE_RESISTANCE.get(layer, 0)
            total += weight * len(items)
            count += len(items)

        if count == 0:
            return 0  # No resistance if nothing triggered

        average = total / count
        return min(int(average), 100)


# Example usage
if __name__ == "__main__":
    estimator = ResistanceLevelEstimator()
    sample_violations = {
        "convictions": ["C1"],
        "principles": ["P2", "P3"],
        "articles": ["A1.1"]
    }
    print("Resistance Level:", estimator.estimate_resistance(sample_violations))  # Example output: ~52
