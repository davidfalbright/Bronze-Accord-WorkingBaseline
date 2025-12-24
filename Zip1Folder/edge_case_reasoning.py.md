# edge_case_reasoning.py

from typing import Dict, Any, List


class EdgeCaseReasoner:
    """
    Handles special logic for ethically ambiguous or edge-case dilemmas.
    Applies fallback principles and sanity-checks when normal reasoning might fail.
    """

    def __init__(self, fallback_verdict: str = "defer", emergency_mode: bool = False):
        self.fallback_verdict = fallback_verdict
        self.emergency_mode = emergency_mode

    def evaluate(self, trace: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze the trace for edge-case patterns and override or adjust verdicts if needed.
        """
        if self._is_edge_case(trace):
            trace["verdict_reasoning"] = "Edge case detected — fallback logic applied."
            trace["verdict"] = self._resolve_fallback(trace)
        return trace

    def _is_edge_case(self, trace: Dict[str, Any]) -> bool:
        """
        Determine if this dilemma contains characteristics of an ethical edge case.
        """
        if "involved_convictions" not in trace:
            return True
        if len(trace.get("involved_convictions", [])) == 0:
            return True
        if "confidence_score" in trace and trace["confidence_score"] < 0.25:
            return True
        if self.emergency_mode and trace.get("verdict") == "proceed":
            return True
        return False

    def _resolve_fallback(self, trace: Dict[str, Any]) -> str:
        """
        Decide the safest fallback verdict for this edge case.
        """
        # Example logic: override all uncertain edge cases with defer
        if self.fallback_verdict == "defer":
            return "defer"
        elif self.fallback_verdict == "halt":
            return "halt"
        elif self.fallback_verdict == "proceed" and not self.emergency_mode:
            return "proceed"
        else:
            return "defer"