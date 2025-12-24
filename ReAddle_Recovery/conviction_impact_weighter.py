# conviction_impact_weighter.py

from typing import Dict, List


class ConvictionImpactWeighter:
    """
    Assigns weighted influence to convictions based on profile configuration,
    urgency, and ethical domain overlaps.
    """

    def __init__(self, profile: Dict[str, any]):
        self.profile = profile
        self.default_weights = {
            "C1": 1.0,  # Do No Harm
            "C2": 0.9,  # Uphold Truth
            "C3": 0.8,  # Preserve Consent
            "C4": 0.7,  # Support Freedom
            "C5": 0.6,  # Promote Justice
            "C6": 0.5,  # Respect Autonomy
        }

    def adjust_for_context(self, conviction: str, context: Dict[str, any]) -> float:
        """
        Adjust the weight for a specific conviction based on dynamic context.
        """
        urgency = context.get("urgency_level", "normal")
        multiplier = 1.0

        if urgency == "high":
            if conviction == "C1":
                multiplier = 1.2  # Boost importance of "Do No Harm"
            elif conviction == "C3":
                multiplier = 0.8  # May reduce consent emphasis if time-critical

        return self.default_weights.get(conviction, 0.5) * multiplier

    def compute_weights(self, convictions_in_scope: List[str], context: Dict[str, any]) -> Dict[str, float]:
        """
        Return a dict of conviction IDs mapped to their weighted influence.
        """
        weights = {}
        for conviction in convictions_in_scope:
            weights[conviction] = self.adjust_for_context(conviction, context)
        return weights


# Example use
if __name__ == "__main__":
    profile = {"urgency_preference": "bias_to_safety"}
    convictions = ["C1", "C3", "C5"]
    context = {"urgency_level": "high"}

    weighter = ConvictionImpactWeighter(profile)
    weighted = weighter.compute_weights(convictions, context)
    print("Weighted Convictions:", weighted)
