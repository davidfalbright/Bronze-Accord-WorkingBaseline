# ===============================
# Module: verdict_conflict_resolver.py
# Purpose: Resolve ethical conflicts when multiple layers or rules
#          produce contradictory outputs
# Part of: Verdict Engine Conflict Resolution Layer
# ===============================

import logging
from framework_models import ConflictSet, ConflictResolutionResult

logger = logging.getLogger(__name__)

RESOLUTION_PRIORITY = ["conviction", "safeguard", "principle", "article"]

def resolve_conflict(conflict: ConflictSet) -> ConflictResolutionResult:
    """
    Apply resolution logic to a detected ethical conflict.

    Args:
        conflict (ConflictSet): Contains multiple competing outputs

    Returns:
        ConflictResolutionResult: Chosen outcome and reasoning
    """
    logger.debug("Resolving conflict across ethical layers...")

    try:
        grouped = {}
        for decision in conflict.candidates:
            layer = decision.layer
            grouped.setdefault(layer, []).append(decision)

        for priority in RESOLUTION_PRIORITY:
            if priority in grouped:
                chosen = grouped[priority][0]
                logger.info(f"Conflict resolved in favor of: {priority} layer.")
                return ConflictResolutionResult(
                    chosen=chosen,
                    method=f"Layer priority: {priority}"
                )

        logger.warning("No conflict resolution match found. Defaulting to first candidate.")
        return ConflictResolutionResult(
            chosen=conflict.candidates[0],
            method="Default to first candidate"
        )

    except Exception as e:
        logger.exception("Conflict resolution failed.")
        return ConflictResolutionResult(
            chosen=None,
            method=f"Error: {str(e)}"
        )
