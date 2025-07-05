# yaml_formatter.py

from typing import List, Dict
import yaml


class YAMLFormatter:
    """
    Converts evaluation results into a YAML-friendly structure.
    """

    def format_verdict(self, verdict: Dict) -> str:
        """
        Converts a verdict dictionary into a YAML-formatted string.

        Args:
            verdict: A dictionary representing the evaluated verdict, including keys like:
                - conflict
                - triggered_elements
                - strength_score
                - severity_level
                - support_details

        Returns:
            A YAML-formatted string.
        """
        # Clean and structure the data
        yaml_ready = {
            "Verdict": {
                "Conflict": {
                    "Description": verdict.get("conflict", {}).get("description", ""),
                    "Source1": verdict.get("conflict", {}).get("source_1", ""),
                    "Source2": verdict.get("conflict", {}).get("source_2", ""),
                    "TriggeredElements": verdict.get("conflict", {}).get("triggered_elements", [])
                },
                "Evaluation": {
                    "StrengthScore": verdict.get("strength_score", 0),
                    "SeverityLevel": verdict.get("severity_level", "unknown"),
                    "SupportingEvidence": verdict.get("supporting_evidence", [])
                }
            }
        }

        return yaml.dump(yaml_ready, sort_keys=False, allow_unicode=True)


# Example usage
if __name__ == "__main__":
    formatter = YAMLFormatter()
    example_verdict = {
        "conflict": {
            "description": "Conflict between Conviction C1 and Principle P4",
            "source_1": "C1",
            "source_2": "P4",
            "triggered_elements": ["C1", "P4"]
        },
        "strength_score": 12,
        "severity_level": "moderate",
        "supporting_evidence": ["Policy match from YAML", "User profile tag match"]
    }

    yaml_output = formatter.format_verdict(example_verdict)
    print(yaml_output)
