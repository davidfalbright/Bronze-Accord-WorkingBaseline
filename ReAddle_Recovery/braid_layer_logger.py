# ===============================
# Module: braid_layer_logger.py
# Purpose: Log entry and exit for each ethical evaluation layer (C/S/P/A),
#          including interim decisions and overrides
# Part of: braid Execution Tracing System
# ===============================

import logging
from datetime import datetime
from typing import List
from framework_models import LayerLogEntry, LayerLog

logger = logging.getLogger(__name__)

class braidLayerLogger:
    """
    Logs decision path across braid ethical layers.
    """

    def __init__(self):
        self.entries: List[LayerLogEntry] = []

    def log_entry(self, layer: str, decision: str, rationale: str, success: bool):
        timestamp = datetime.utcnow().isoformat()
        logger.debug(f"[{layer}] {decision} - success={success}")
        entry = LayerLogEntry(
            layer=layer,
            decision=decision,
            rationale=rationale,
            timestamp=timestamp,
            success=success
        )
        self.entries.append(entry)

    def get_log(self) -> LayerLog:
        return LayerLog(entries=self.entries)
