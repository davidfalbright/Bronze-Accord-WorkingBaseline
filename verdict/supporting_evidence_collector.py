# supporting_evidence_collector.py

from typing import Dict, Any, List

class SupportingEvidenceCollector:
    """
    Gathers relevant evidence that supports or explains the verdict outcome.
    """

    def __init__(self):
        pass

    def collect(self, context: Dict[str, Any], triggered_elements: Dict[str, List[str]]) -> List[str]:
        """
        Produces a list of evidence strings that provide context or justification.

        Args:
            context: The full evaluation context, including dilemma text, reasoning, source metadata, etc.
            triggered_elements: A dictionary of which ethical elements (Convictions, Safeguards, etc.) were triggered.

        Returns:
            A list of strings summarizing or quoting supporting insights.
        """
        evidence = []

        # Example: Pull insight text from context
        for category, ids in triggered_elements.items():
            for eid in ids:
                insight = context.get("insights", {}).get(eid)
                if insight:
                    evidence.append(f"{category.upper()} {eid}: {insight}")

        # Fallback if no insight text is available
        if not evidence:
            evidence.append("No explicit insight text available. Verdict inferred from pattern alignment and severity logic.")

        return evidence


# Example usage
if __name__ == "__main__":
    ctx = {
        "insights": {
            "C1": "Do no harm to sentient beings.",
            "S3": "Avoid actions that exploit informational asymmetry."
        }
    }
    triggered = {
        "convictions": ["C1"],
        "safeguards": ["S3"]
    }

    collector = SupportingEvidenceCollector()
    print(collector.collect(ctx, triggered))
