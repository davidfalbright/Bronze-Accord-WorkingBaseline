# verdict_priority_sorter.py

from typing import List, Dict


class VerdictPrioritySorter:
    """
    Sorts a list of verdicts based on severity, urgency, and conviction strength.
    Designed for reconciliation and display prioritization.
    """

    @staticmethod
    def sort_verdicts(verdicts: List[Dict]) -> List[Dict]:
        """
        Sorts the verdicts using a weighted priority system.
        Priority is determined in this order:
        1. Verdict strength (descending)
        2. Urgency (descending)
        3. Conviction strength (descending)
        """
        return sorted(
            verdicts,
            key=lambda v: (
                v.get("verdict_strength", 0),
                v.get("urgency", 0),
                v.get("conviction_strength", 0)
            ),
            reverse=True
        )
