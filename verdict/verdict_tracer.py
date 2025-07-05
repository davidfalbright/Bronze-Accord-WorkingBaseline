# ===============================
# Module: verdict_tracer.py
# Purpose: Trace internal flow of ethical evaluation across layers
#          and preserve each decision branch considered
# Part of: Verdict Engine Trace Layer
# ===============================

import logging
from typing import List
from framework_models import TraceStep, VerdictTrace

logger = logging.getLogger(__name__)

class VerdictTracer:
    """
    Tracks decisions across evaluation layers.
    """

    def __init__(self):
        self.steps: List[TraceStep] = []

    def record(self, layer: str, rule_id: str, result: str, rationale: str):
        logger.debug(f"[TRACE] {layer} > {rule_id}: {result}")
        self.steps.append(TraceStep(
            layer=layer,
            rule_id=rule_id,
            result=result,
            rationale=rationale
        ))

    def get_trace(self) -> VerdictTrace:
        return VerdictTrace(steps=self.steps)
