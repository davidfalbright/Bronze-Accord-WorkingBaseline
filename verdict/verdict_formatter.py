# verdict_formatter.py

from typing import Dict, List
from framework_models import EvaluatedVerdict


class VerdictFormatter:
    """
    Formats the EvaluatedVerdict into a standardized dictionary suitable for API response or storage.
    """

    def __init__(self):
        pass

    def format(self, verdict: EvaluatedVerdict) -> Dict:
        """
        Converts the internal EvaluatedVerdict object into a structured dictionary.

        Args:
            verdict: An EvaluatedVerdict object containing verdict details.

        Returns:
            A dictionary representation of the verdict.
        """
        return {
            "conflict": {
                "source_1": verdict.conflict.source_1,
                "source_2": verdict.conflict.source_2,
                "description": verdict.conflict.description,
                "triggered_elements": verdict.conflict.triggered_elements
            },
            "verdict_summary": {
                "strength_score": verdict.strength_score,
                "severity_level": verdict.severity_level,
                "supporting_evidence": verdict.supporting_evidence
            }
        }


# Example usage
if __name__ == "__main__":
    from framework_models import ConflictMetadata

    dummy_conflict = ConflictMetadata(
        source_1="Judaism",
        source_2="Bronze Accord",
        description="Article A1.2 violates Safeguard S4",
        triggered_elements={
            "safeguards": ["S4"],
            "articles": ["A1.2"]
        }
    )

    dummy_verdict = EvaluatedVerdict(
        conflict=dummy_conflict,
        strength_score=8,
        severity_level="High",
        supporting_evidence=[
            {"component_id": "S4", "component_type": "safeguard", "rationale": "Non-coercion principle violated"}
        ]
    )

    formatter = VerdictFormatter()
    print("Formatted Verdict:\n", formatter.format(dummy_verdict))
