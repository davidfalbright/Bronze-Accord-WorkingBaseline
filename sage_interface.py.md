# ===============================
# Module: sage_interface.py
# Purpose: Define a consistent interface between the braid system and
#          external symbolic or statistical reasoning engines (SAGE)
# Part of: SAGELINK Integration Layer
# ===============================

import logging
from framework_models import ParsedInput, SageRequest, SageResponse

logger = logging.getLogger(__name__)

def prepare_sage_request(parsed: ParsedInput) -> SageRequest:
    """
    Convert braid-parsed input into a SAGE-compatible request.

    Args:
        parsed (ParsedInput): Structured ethical input.

    Returns:
        SageRequest: Encapsulated format for symbolic engines.
    """
    logger.debug("Preparing SAGE request payload...")

    structured = parsed.structured
    symbols = structured.get("keywords", []) + structured.get("tags", [])

    return SageRequest(
        original_input=parsed,
        extracted_symbols=symbols,
        use_inference=True
    )


def interpret_sage_response(response: SageResponse) -> str:
    """
    Interpret the results returned from a SAGE reasoning engine.

    Args:
        response (SageResponse): Output from SAGE system.

    Returns:
        str: Summary of SAGE interpretation for braid logging.
    """
    logger.debug("Interpreting SAGE response...")
    return f"SAGE flagged {len(response.violated_rules)} violations and suggested '{response.suggestion}'"