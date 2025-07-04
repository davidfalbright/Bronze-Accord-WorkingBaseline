# ethical_scope_calculator.py

from typing import List, Dict, Any


class EthicalScopeCalculator:
    """
    Determines which domains, beliefs, or convictions are in scope for a given ethical evaluation.
    """

    def __init__(self, profile: Dict[str, Any]):
        self.profile = profile

    def evaluate_scope(self, dilemma_text: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze the dilemma and profile context to determine which ethical domains apply.
        """
        in_scope = {
            "convictions": [],
            "principles": [],
            "safeguards": [],
            "articles": [],
        }

        # Placeholder logic - this would be replaced by actual NLP/semantic matching
        keywords = dilemma_text.lower().split()
        conviction_map = {
            "harm": "C1",
            "truth": "C2",
            "consent": "C3",
            "freedom": "C4",
            "justice": "C5",
            "autonomy": "C6",
        }

        for word in keywords:
            if word in conviction_map:
                in_scope["convictions"].append(conviction_map[word])

        # Add profile-specific adjustments
        if context.get("urgency_level") == "high":
            in_scope["safeguards"].append("S1")

        return in_scope

    def expand_scope(self, initial_scope: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add inferred ethical elements based on the initial scope.
        """
        expanded = dict(initial_scope)
        if "C1" in initial_scope["convictions"]:
            expanded["principles"].append("P1")
            expanded["articles"].append("A1.1")

        return expanded


# Example usage
if __name__ == "__main__":
    calc = EthicalScopeCalculator(profile={"role": "AI"})
    dilemma = "Should the system intervene if harm is imminent but the user has not given consent?"
    context = {"urgency_level": "high"}
    scope = calc.evaluate_scope(dilemma, context)
    expanded = calc.expand_scope(scope)
    print("Initial Scope:", scope)
    print("Expanded Scope:", expanded)