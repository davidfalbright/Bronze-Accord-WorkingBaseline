# ===============================
# Module: yaml_term_mapper.py
# Purpose: Map ethical Charter terms to equivalent synonyms and concepts
#          within the YAML block to improve semantic alignment
# Part of: YAML Semantic Matching Layer
# ===============================

import logging
from framework_models import TermMappingResult

logger = logging.getLogger(__name__)

SYNONYM_MAP = {
    "autonomy": ["freedom", "self-determination", "consent"],
    "transparency": ["openness", "explainability", "visibility"],
    "justice": ["fairness", "equity", "due process"],
    "harm": ["injury", "suffering", "damage"],
    "power": ["control", "influence", "authority"]
}

def map_term_to_yaml(term: str) -> TermMappingResult:
    """
    Translate a Charter concept to all matching YAML terms.

    Args:
        term (str): Ethical keyword or value from the Charter

    Returns:
        TermMappingResult: List of matched terms with context
    """
    logger.debug(f"Mapping term '{term}' to YAML equivalents...")

    normalized = term.strip().lower()
    synonyms = SYNONYM_MAP.get(normalized, [])

    success = bool(synonyms)
    return TermMappingResult(
        term=term,
        synonyms=synonyms,
        success=success
    )