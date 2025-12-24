# verdict_verdict_combiner.py

from typing import List
from framework_models import EvaluatedVerdict


class VerdictCombiner:
    """
    Combines multiple EvaluatedVerdict objects into a unified summary.
    Useful when multiple sub-decisions or micro-conflicts are part of a larger ethical evaluation.
    """

    def combine(self, verdicts: List[EvaluatedVerdict]) -> EvaluatedVerdict:
        if not verdicts:
            raise ValueError("No verdicts to combine.")

        # Use the first conflict as representative, but we may eventually want to union all
        combined_conflict = verdicts[0].conflict
        combined_elements = set()
        all_evidence = []
        total_strength = 0
        max_severity = 0

        for v in verdicts:
            combined_elements.update(v.conflict.triggered_elements)
            all_evidence.extend(v.supporting_evidence)
            total_strength += v.strength_score
            max_severity = max(max_severity, v.severity_level)

        # Create new combined verdict
        combined_conflict.triggered_elements = list(combined_elements)
        return EvaluatedVerdict(
            conflict=combined_conflict,
            strength_score=total_strength,
            severity_level=max_severity,
            supporting_evidence=all_evidence
        )


# Example usage
if __name__ == "__main__":
    # This part is stubbed, assuming EvaluatedVerdict objects are created upstream
    print("This module should be tested via integration with verdict evaluator pipeline.")
