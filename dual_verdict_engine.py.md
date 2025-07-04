# dual_verdict_engine.py

from typing import List, Dict
from framework_models import EthicalConflict, EvaluatedVerdict
from verdict_strength_calculator import VerdictStrengthCalculator
from moral_resistance_calculator import MoralResistanceCalculator
from decision_difficulty_evaluator import DecisionDifficultyEvaluator
from severity_level_classifier import SeverityLevelClassifier
from evidence_integrity_checker import EvidenceIntegrityChecker


class DualVerdictEngine:
    """
    Processes ethical conflicts and issues dual verdicts: one from the Accord’s ethical logic,
    and one simulating a real-world moral baseline (e.g., utilitarian or cultural norm).
    """

    def __init__(self):
        self.strength_calc = VerdictStrengthCalculator()
        self.resistance_calc = MoralResistanceCalculator()
        self.difficulty_eval = DecisionDifficultyEvaluator()
        self.severity_classifier = SeverityLevelClassifier()
        self.integrity_checker = EvidenceIntegrityChecker()

    def evaluate_conflict(self, conflict: EthicalConflict) -> Dict[str, EvaluatedVerdict]:
        """
        Evaluates a conflict and returns dual verdicts.

        Args:
            conflict: The ethical conflict to evaluate.

        Returns:
            A dictionary with two EvaluatedVerdict entries:
              - 'accord_verdict': Evaluated according to Bronze Accord logic
              - 'baseline_verdict': Evaluated according to a generic moral baseline
        """
        # Step 1: Calculate metrics
        strength_score = self.strength_calc.calculate_strength(conflict.triggered_elements)
        resistance_level = self.resistance_calc.calculate_resistance(conflict.triggered_elements)
        difficulty_level = self.difficulty_eval.evaluate(conflict)
        severity_level = self.severity_classifier.classify(conflict.triggered_elements)
        integrity_score = self.integrity_checker.check(conflict.supporting_evidence)

        # Step 2: Compose primary Accord verdict
        accord_verdict = EvaluatedVerdict(
            conflict=conflict,
            strength_score=strength_score,
            resistance_level=resistance_level,
            severity_level=severity_level,
            difficulty_level=difficulty_level,
            supporting_evidence=conflict.supporting_evidence,
            verdict_basis="Bronze Accord Framework",
            evidence_integrity_score=integrity_score
        )

        # Step 3: Generate baseline verdict (for comparison)
        baseline_strength = min(strength_score, 3)  # Cap at 3 to simulate lower ethical standard
        baseline_resistance = resistance_level - 1 if resistance_level > 0 else 0
        baseline_difficulty = max(difficulty_level - 1, 0)
        baseline_verdict = EvaluatedVerdict(
            conflict=conflict,
            strength_score=baseline_strength,
            resistance_level=baseline_resistance,
            severity_level="Moderate",
            difficulty_level=baseline_difficulty,
            supporting_evidence=conflict.supporting_evidence,
            verdict_basis="Generic Ethical Baseline",
            evidence_integrity_score=integrity_score
        )

        return {
            "accord_verdict": accord_verdict,
            "baseline_verdict": baseline_verdict
        }


# Example usage (mocked)
if __name__ == "__main__":
    conflict = EthicalConflict(
        source_1="AI Decision",
        source_2="Human Value",
        triggered_elements={
            "convictions": ["C1"],
            "principles": ["P1", "P4"]
        },
        description="Conflict between AI override and human autonomy.",
        supporting_evidence=["Bronze Accord Charter: C1", "Academic Canon: Free Will"]
    )

    engine = DualVerdictEngine()
    verdicts = engine.evaluate_conflict(conflict)
    for label, verdict in verdicts.items():
        print(f"\n{label.upper()}:\n{verdict}")