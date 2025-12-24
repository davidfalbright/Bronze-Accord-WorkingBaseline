# ===============================
# Module: verdict_layer_report.py
# Purpose: Compile a report summarizing how each ethical layer
#          contributed to the final verdict
# Part of: Verdict Engine Reporting Layer
# ===============================

import logging
from framework_models import LayerContribution, LayerReport, EngineOutcome

logger = logging.getLogger(__name__)

def generate_layer_report(outcome: EngineOutcome) -> LayerReport:
    """
    Generate a report showing how each ethical layer factored into the verdict.

    Args:
        outcome (EngineOutcome): Final verdict engine result.

    Returns:
        LayerReport: Contribution summary per layer.
    """
    logger.debug("Generating layer contribution report...")

    if not outcome.success or not outcome.verdict:
        return LayerReport(
            success=False,
            contributions=[],
            message="No valid verdict to report on."
        )

    contributions = []

    triggered = getattr(outcome.verdict, "triggered_elements", [])
    for eid in triggered:
        layer_type = classify_element_type(eid)
        contributions.append(
            LayerContribution(
                layer=layer_type,
                element_id=eid,
                weight=calculate_layer_weight(layer_type)
            )
        )

    return LayerReport(success=True, contributions=contributions)


def classify_element_type(element_id: str) -> str:
    if element_id.startswith("C"):
        return "conviction"
    if element_id.startswith("S"):
        return "safeguard"
    if element_id.startswith("P"):
        return "principle"
    if element_id.startswith("A"):
        return "article"
    return "unknown"


def calculate_layer_weight(layer: str) -> float:
    weights = {
        "conviction": 1.0,
        "safeguard": 0.9,
        "principle": 0.7,
        "article": 0.5,
        "unknown": 0.1
    }
    return weights.get(layer, 0.1)
