# ethical_conflict_resolver.py

from typing import List
from framework_models import EthicalConflict
from dual_verdict_engine import DualVerdictEngine
from verdict_logger import VerdictLogger


class EthicalConflictResolver:
    """
    High-level interface for resolving a list of ethical conflicts.
    Delegates evaluation to the DualVerdictEngine and manages result logging.
    """

    def __init__(self):
        self.engine = DualVerdictEngine()
        self.logger = VerdictLogger()

    def resolve_conflicts(self, conflicts: List[EthicalConflict]) -> List[dict]:
        """
        Processes a list of ethical conflicts and logs the results.

        Args:
            conflicts: A list of EthicalConflict instances.

        Returns:
            A list of dictionaries containing 'accord_verdict' and 'baseline_verdict' for each conflict.
        """
        verdicts_list = []

        for conflict in conflicts:
            dual_verdicts = self.engine.evaluate_conflict(conflict)
            self.logger.log_verdict(dual_verdicts["accord_verdict"])
            self.logger.log_verdict(dual_verdicts["baseline_verdict"])
            verdicts_list.append(dual_verdicts)

        return verdicts_list


# Example usage (mocked)
if __name__ == "__main__":
    sample_conflict = EthicalConflict(
        source_1="Algorithmic Override",
        source_2="Cultural Norm",
        triggered_elements={
            "convictions": ["C2"],
            "safeguards": ["S1"],
            "principles": ["P1"],
            "articles": ["A1.1"]
        },
        description="System override triggered despite normative expectations.",
        supporting_evidence=["Charter Excerpt", "Public Policy Memo"]
    )

    resolver = EthicalConflictResolver()
    outcomes = resolver.resolve_conflicts([sample_conflict])

    for outcome in outcomes:
        print("ACCORD VERDICT:", outcome["accord_verdict"])
        print("BASELINE VERDICT:", outcome["baseline_verdict"])
