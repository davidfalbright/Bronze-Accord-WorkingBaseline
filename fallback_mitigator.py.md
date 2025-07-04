# fallback_mitigator.py

from typing import Any, Dict


class FallbackMitigator:
    """
    Provides safe fallback behavior in case the verdict engine,
    resistance calculator, or any core ethical evaluator fails or returns ambiguity.
    """

    def __init__(self):
        self.default_verdict = {
            "verdict": "undecided",
            "strength": 0.0,
            "resistance": 0.0,
            "triggered_elements": [],
            "explanation": "Fallback invoked due to error or insufficient data."
        }

    def mitigate(self, error_context: Dict[str, Any] = None) -> Dict:
        """
        Returns a standardized fallback verdict response.

        Args:
            error_context (Dict[str, Any], optional): Info about what failed.

        Returns:
            Dict: Standard fallback verdict
        """
        explanation = self.default_verdict["explanation"]
        if error_context and "error" in error_context:
            explanation += f" Reason: {error_context['error']}"

        return {
            **self.default_verdict,
            "context_details": error_context or {},
            "explanation": explanation
        }