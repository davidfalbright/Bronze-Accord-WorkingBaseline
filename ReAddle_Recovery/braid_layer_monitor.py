# ===============================
# Module: braid_layer_monitor.py
# Purpose: Track which ethical layers were evaluated during a verdict run,
#          capturing order, time spent, and any failures encountered
# Part of: braid Diagnostics and Auditing
# ===============================

import logging
from framework_models import LayerMonitorLog, EvaluationStep

logger = logging.getLogger(__name__)

class braidLayerMonitor:
    """
    Tracks evaluation progress through each ethical layer.
    """

    def __init__(self):
        self.steps = []

    def record_step(self, layer: str, duration_ms: int, status: str, notes: str = ""):
        logger.debug(f"Recording step: {layer}, {status}, {duration_ms}ms")
        self.steps.append(EvaluationStep(
            layer=layer,
            duration_ms=duration_ms,
            status=status,
            notes=notes
        ))

    def export_log(self) -> LayerMonitorLog:
        logger.info("Exporting braid layer monitor log.")
        return LayerMonitorLog(steps=self.steps)
