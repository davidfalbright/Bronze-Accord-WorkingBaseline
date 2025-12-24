# ===============================
# Module: sage_translator.py
# Purpose: Translate between braid's ethical data format and SAGE's
#          symbolic reasoning schema (e.g. logic rule language)
# Part of: SAGELINK Translation Layer
# ===============================

import logging
from framework_models import SageRequest, SageSymbolSet

logger = logging.getLogger(__name__)

def translate_to_sage_symbols(request: SageRequest) -> SageSymbolSet:
    """
    Convert extracted keywords/tags into formal SAGE symbols.

    Args:
        request (SageRequest): Prepared SAGE-compatible request.

    Returns:
        SageSymbolSet: List of encoded symbols for rule processing.
    """
    logger.debug("Translating to SAGE symbols...")

    symbols = []
    for raw in request.extracted_symbols:
        symbol = encode_symbol(raw)
        symbols.append(symbol)

    return SageSymbolSet(symbols=symbols)


def encode_symbol(raw: str) -> str:
    """
    Convert a natural language keyword into a formal symbolic form.

    Args:
        raw (str): Raw tag or keyword from ethical input.

    Returns:
        str: Encoded SAGE-compatible symbol
    """
    return raw.strip().lower().replace(" ", "_")
