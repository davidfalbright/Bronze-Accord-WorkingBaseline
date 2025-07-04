# api_response_formatter.py

from framework_models import EvaluatedVerdict
from typing import Dict


class APIResponseFormatter:
    """
    Formats evaluated verdicts into JSON-serializable API response structures.
    """

    @staticmethod
    def format(verdict: EvaluatedVerdict) -> Dict:
        return {
            "conflict": {
                "source_1": verdict.conflict.source_1,
                "source_2": verdict.conflict.source_2,
                "triggered_elements": verdict.conflict.triggered_elements,
                "description": verdict.conflict.description
            },
            "strength_score": verdict.strength_score,
            "severity_level": verdict.severity_level,
            "supporting_evidence": verdict.supporting_evidence
        }

    @staticmethod
    def format_dual(dual_verdicts: Dict[str, EvaluatedVerdict]) -> Dict:
        return {
            "accord_verdict": APIResponseFormatter.format(dual_verdicts["accord_verdict"]),
            "baseline_verdict": APIResponseFormatter.format(dual_verdicts["baseline_verdict"])
        }