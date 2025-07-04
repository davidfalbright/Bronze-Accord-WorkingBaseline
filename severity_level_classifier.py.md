# severity_level_classifier.py

class SeverityLevelClassifier:
    """
    Classifies the overall ethical severity of a dilemma based on the verdict strength
    and decision difficulty.
    """

    def __init__(self):
        # Default thresholds; these can be configured dynamically if needed.
        self.thresholds = {
            "low": (0, 10),
            "moderate": (11, 25),
            "high": (26, 45),
            "critical": (46, float("inf"))
        }

    def classify(self, verdict_strength: int, decision_difficulty: int) -> str:
        """
        Combines verdict strength and decision difficulty to classify severity.

        Args:
            verdict_strength (int): Strength score of the ethical evaluation.
            decision_difficulty (int): Difficulty score based on conflicting elements.

        Returns:
            str: Severity label ('low', 'moderate', 'high', or 'critical')
        """
        total_score = verdict_strength + decision_difficulty

        for label, (min_score, max_score) in self.thresholds.items():
            if min_score <= total_score <= max_score:
                return label

        return "unknown"


# Example usage
if __name__ == "__main__":
    classifier = SeverityLevelClassifier()
    severity = classifier.classify(verdict_strength=20, decision_difficulty=15)
    print("Severity Level:", severity)  # Should print 'high'