# urgency_classifier.py

from typing import Dict, Any


class UrgencyClassifier:
    """
    Determines the urgency level of an ethical dilemma based on its content
    and triggered ethical components.
    """

    def __init__(self, config: Dict[str, Any] = None):
        """
        Optional configuration dictionary may include urgency keywords and thresholds.
        """
        self.config = config or {
            "high_urgency_keywords": ["imminent", "immediate", "life-threatening", "emergency", "critical"],
            "medium_urgency_keywords": ["soon", "delayed", "pending", "sensitive"],
        }

    def classify(self, dilemma_text: str, triggered: Dict[str, list]) -> str:
        """
        Assigns an urgency level: HIGH, MEDIUM, or LOW.
        Logic considers both keywords and the types of components triggered.
        """
        text = dilemma_text.lower()

        # Keyword scan
        for word in self.config["high_urgency_keywords"]:
            if word in text:
                return "HIGH"
        for word in self.config["medium_urgency_keywords"]:
            if word in text:
                return "MEDIUM"

        # Fallback to component-based inference
        if "C1" in triggered.get("convictions", []) or "S1" in triggered.get("safeguards", []):
            return "HIGH"
        elif triggered.get("convictions") or triggered.get("safeguards"):
            return "MEDIUM"
        else:
            return "LOW"


# Example usage
if __name__ == "__main__":
    classifier = UrgencyClassifier()
    dilemma = "This is a critical and immediate situation involving harm."
    example_triggered = {"convictions": ["C1"], "safeguards": ["S1"], "principles": [], "articles": []}
    print("Urgency:", classifier.classify(dilemma, example_triggered))