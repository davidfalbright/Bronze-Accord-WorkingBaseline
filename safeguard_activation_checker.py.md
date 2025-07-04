# safeguard_activation_checker.py

from typing import List, Dict


class SafeguardActivationChecker:
    """
    Determines which safeguards were activated during a verdict evaluation.
    This is useful for logging, reporting, and enforcement traceability.
    """

    def __init__(self, safeguard_registry: Dict[str, dict]):
        """
        Args:
            safeguard_registry: A dictionary mapping safeguard IDs (e.g., "S1", "S4") to their full definitions.
        """
        self.registry = safeguard_registry

    def check_activation(self, triggered_ids: List[str]) -> List[dict]:
        """
        Returns detailed info about which safeguards were triggered.

        Args:
            triggered_ids: List of string IDs from the conflict verdict.

        Returns:
            List of dictionaries with full safeguard metadata.
        """
        results = []
        for sid in triggered_ids:
            if sid.startswith("S") and sid in self.registry:
                results.append(self.registry[sid])
        return results


# Example usage
if __name__ == "__main__":
    registry = {
        "S1": {"id": "S1", "description": "Do not cause suffering"},
        "S2": {"id": "S2", "description": "Respect autonomy"}
    }
    checker = SafeguardActivationChecker(registry)
    triggered = ["C1", "S1", "S2", "A1.3"]
    print("Activated safeguards:", checker.check_activation(triggered))