# verdict_output_formatter.py

from typing import Dict


class VerdictOutputFormatter:
    """
    Formats the evaluated verdict for standardized display or API response.
    """

    def __init__(self):
        pass

    def format(self, verdict_dict: Dict) -> Dict:
        """
        Converts an evaluated verdict dictionary into a standardized output structure.

        Args:
            verdict_dict: Raw internal verdict structure.

        Returns:
            Formatted verdict dictionary for API or UI consumption.
        """
        formatted = {
            "conflict_description": verdict_dict["conflict"]["description"],
            "triggered_elements": verdict_dict["conflict"]["triggered_elements"],
            "verdict_strength": verdict_dict["verdict_summary"]["strength_score"],
            "severity_level": verdict_dict["verdict_summary"]["severity_level"],
            "evidence": verdict_dict["verdict_summary"].get("supporting_evidence", []),
            "source_1": verdict_dict["conflict"]["source_1"],
            "source_2": verdict_dict["conflict"]["source_2"]
        }
        return formatted


# Example usage
if __name__ == "__main__":
    formatter = VerdictOutputFormatter()

    example_verdict = {
        "conflict": {
            "source_1": "Islam",
            "source_2": "Bronze Accord",
            "description": "Violation of Principle P1",
            "triggered_elements": {
                "principles": ["P1"]
            }
        },
        "verdict_summary": {
            "strength_score": 5,
            "severity_level": "Moderate",
            "supporting_evidence": ["Islamic source text A vs Bronze Accord P1"]
        }
    }

    output = formatter.format(example_verdict)
    print("Formatted Verdict:", output)