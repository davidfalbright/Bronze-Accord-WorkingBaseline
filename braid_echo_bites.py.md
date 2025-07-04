# ===============================
# Module: braid_echo_bites.py
# Purpose: Return short-form summaries ("echo bites") of the verdict logic,
#          emphasizing which safeguards or convictions were triggered
# Part of: braid Echo System
# ===============================

import logging
from framework_models import EngineOutcome, EchoBite

logger = logging.getLogger(__name__)

def generate_echo_bite(outcome: EngineOutcome) -> EchoBite:
    """
    Generate a brief, human-readable summary of the verdict path.

    Args:
        outcome (EngineOutcome): Final verdict result with context.

    Returns:
        EchoBite: Condensed summary highlighting ethical elements used.
    """
    logger.debug("Generating echo bite summary...")
    try:
        if not outcome.success or not outcome.verdict:
            return EchoBite(text="No verdict available.", success=False)

        elements = outcome.verdict.triggered_elements or []
        short_summary = f"Decision: {outcome.verdict.decision}. " \
                        f"Driven by: {', '.join(elements) or 'unspecified rationale'}."

        return EchoBite(text=short_summary, success=True)

    except Exception as e:
        logger.exception("Failed to generate echo bite.")
        return EchoBite(text=str(e), success=False)