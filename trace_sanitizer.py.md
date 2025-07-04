# trace_sanitizer.py

from typing import Dict


class TraceSanitizer:
    """
    Sanitizes a full verdict trace before export or storage by:
    - Removing sensitive content
    - Trimming large fields
    - Ensuring consistency and readability
    """

    def __init__(self, max_field_length: int = 200):
        self.max_length = max_field_length

    def sanitize_trace(self, trace: Dict) -> Dict:
        sanitized = dict(trace)

        # Sanitize rationale
        if "rationale" in sanitized:
            sanitized["rationale"] = self._truncate(sanitized["rationale"])

        # Sanitize steps
        if "steps" in sanitized:
            sanitized["steps"] = [self._sanitize_step(s) for s in sanitized["steps"]]

        # Sanitize source beliefs
        if "source_beliefs" in sanitized:
            sanitized["source_beliefs"] = [self._sanitize_belief(b) for b in sanitized["source_beliefs"]]

        return sanitized

    def _sanitize_step(self, step: Dict) -> Dict:
        step_copy = dict(step)
        if "description" in step_copy:
            step_copy["description"] = self._truncate(step_copy["description"])
        if "data" in step_copy and isinstance(step_copy["data"], dict):
            step_copy["data"] = {k: self._truncate(str(v)) for k, v in step_copy["data"].items()}
        return step_copy

    def _sanitize_belief(self, belief: Dict) -> Dict:
        belief_copy = dict(belief)
        if "insight_text" in belief_copy:
            belief_copy["insight_text"] = self._truncate(belief_copy["insight_text"])
        if "source" in belief_copy:
            belief_copy["source"] = self._truncate(belief_copy["source"])
        return belief_copy

    def _truncate(self, value: str) -> str:
        if len(value) <= self.max_length:
            return value
        return value[:self.max_length] + "..."