# verdict_trace_builder.py

from typing import Dict, List, Optional


class VerdictTraceBuilder:
    """
    Builds a full trace of how a verdict was reached, including source beliefs,
    triggered elements, and the rationale used for ethical evaluation.
    """

    def __init__(self):
        self.trace: Dict = {}

    def start_trace(self, action_id: str):
        self.trace = {
            "action_id": action_id,
            "steps": [],
            "triggered_elements": [],
            "rationale": "",
            "source_beliefs": []
        }

    def add_step(self, description: str, data: Optional[Dict] = None):
        step = {"description": description}
        if data:
            step.update({"data": data})
        self.trace["steps"].append(step)

    def set_triggered_elements(self, elements: List[str]):
        self.trace["triggered_elements"] = elements

    def set_rationale(self, rationale: str):
        self.trace["rationale"] = rationale

    def set_source_beliefs(self, beliefs: List[Dict]):
        self.trace["source_beliefs"] = beliefs

    def get_trace(self) -> Dict:
        return self.trace