# contextual_rebuttal_analyzer.py

from typing import Dict, List


class ContextualRebuttalAnalyzer:
    """
    Analyzes contextual rebuttals that may arise from contradictions,
    counterarguments, or conflicting ethical sources.
    """

    def __init__(self):
        self.rebuttal_sources = []

    def register_rebuttal_sources(self, sources: List[str]):
        """
        Add known sources of rebuttals for context-aware evaluation.
        """
        self.rebuttal_sources.extend(sources)

    def analyze(self, context: Dict, input_statement: str) -> Dict:
        """
        Analyze for contextual rebuttals based on input and prior context.

        Args:
            context (Dict): The ethical, historical, or situational context.
            input_statement (str): The proposed ethical position.

        Returns:
            Dict: Rebuttal result with 'is_conflict', 'explanation', and 'severity'
        """
        conflicts = []
        severity = 0

        for source in self.rebuttal_sources:
            if source.lower() in input_statement.lower():
                conflicts.append(source)
                severity += 1

        result = {
            "is_conflict": len(conflicts) > 0,
            "conflicts_detected": conflicts,
            "severity": severity,
            "explanation": (
                f"Potential conflict with known rebuttal sources: {', '.join(conflicts)}"
                if conflicts else "No contextual rebuttals detected."
            )
        }

        return result
