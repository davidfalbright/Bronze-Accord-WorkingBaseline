# ===============================
# Module: logger_adapter.py
# Purpose: Provide structured logging helpers for key system
#          events and ethical trace output
# Part of: System Logging Adapter Layer
# ===============================

import logging
from framework_models import TraceStep, LayerContribution

logger = logging.getLogger(__name__)

def log_trace_step(step: TraceStep):
    """
    Log a single ethical evaluation step in structured format.

    Args:
        step (TraceStep): Layer evaluation details.
    """
    logger.info(f"[TRACE] Layer: {step.layer} | Rule: {step.rule_id} | Result: {step.result} | Rationale: {step.rationale}")


def log_contribution(contrib: LayerContribution):
    """
    Log contribution of an ethical layer element.

    Args:
        contrib (LayerContribution): Element ID and weight.
    """
    logger.info(f"[LAYER] {contrib.layer.upper()} triggered {contrib.element_id} (weight: {contrib.weight})")
