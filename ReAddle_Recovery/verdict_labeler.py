# verdict_labeler.py

from typing import Tuple


class VerdictLabeler:
    """
    Converts numerical strength and resistance scores into categorical labels.
    """

    def __init__(self):
        # Thresholds can be fine-tuned later or exposed as config
        self.strength_thresholds = {
            "Low": (0, 5),
            "Medium": (6, 15),
            "High": (16, 30),
            "Extreme": (31, float("inf"))
        }

        self.resistance_thresholds = {
            "None": (0, 0),
            "Weak": (1, 10),
            "Moderate": (11, 20),
            "Strong": (21, 35),
            "Overwhelming": (36, float("inf"))
        }

    def label_strength(self, score: int) -> str:
        for label, (low, high) in self.strength_thresholds.items():
            if low <= score <= high:
                return label
        return "Unknown"

    def label_resistance(self, score: int) -> str:
        for label, (low, high) in self.resistance_thresholds.items():
            if low <= score <= high:
                return label
        return "Unknown"


# Example usage
if __name__ == "__main__":
    labeler = VerdictLabeler()
    print("Strength Label:", labeler.label_strength(17))     # Should return "High"
    print("Resistance Label:", labeler.label_resistance(22)) # Should return "Strong"
