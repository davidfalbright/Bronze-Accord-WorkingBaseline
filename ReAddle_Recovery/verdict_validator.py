# verdict_validator.py

from typing import List, Dict


class VerdictValidator:
    """
    Validates the structure and content of a verdict to ensure it meets framework requirements.
    """

    REQUIRED_KEYS = {"conflict", "verdict_summary"}
    REQUIRED_CONFLICT_KEYS = {"source_1", "source_2", "description", "triggered_elements"}
    REQUIRED_VERDICT_KEYS = {"strength_score", "severity_level", "supporting_evidence"}

    def __init__(self):
        pass

    def validate(self, verdict_dict: Dict) -> List[str]:
        """
        Validates the verdict dictionary structure.

        Args:
            verdict_dict: The verdict dictionary to validate.

        Returns:
            A list of error messages, empty if valid.
        """
        errors = []

        # Top-level check
        for key in self.REQUIRED_KEYS:
            if key not in verdict_dict:
                errors.append(f"Missing top-level key: {key}")

        # Nested structure checks
        if "conflict" in verdict_dict:
            for key in self.REQUIRED_CONFLICT_KEYS:
                if key not in verdict_dict["conflict"]:
                    errors.append(f"Missing conflict key: {key}")

        if "verdict_summary" in verdict_dict:
            for key in self.REQUIRED_VERDICT_KEYS:
                if key not in verdict_dict["verdict_summary"]:
                    errors.append(f"Missing verdict_summary key: {key}")

        return errors


# Example usage
if __name__ == "__main__":
    validator = VerdictValidator()

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
            "supporting_evidence": []
        }
    }

    print("Validation Errors:", validator.validate(example_verdict))  # Should return []
