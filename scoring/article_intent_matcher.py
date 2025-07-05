# ===============================
# Module: article_intent_matcher.py
# Purpose: Match parsed ethical input against specific Articles and their
#          documented Intents to determine likely alignment or conflict
# Part of: Scoring and Intent Mapping
# ===============================

import logging
from framework_models import ParsedInput, IntentMatchResult

logger = logging.getLogger(__name__)

ARTICLE_INTENT_DATABASE = {
    "A1": "protect dignity",
    "A2": "prevent coercion",
    "A3": "ensure accountability",
    "A4": "support human agency",
    "A5": "enable verifiability",
    "A6": "guarantee transparency"
}

def match_article_intents(parsed: ParsedInput) -> IntentMatchResult:
    """
    Attempt to match parsed input to one or more Articles via their stated Intents.

    Args:
        parsed (ParsedInput): Structured ethical input.

    Returns:
        IntentMatchResult: List of article IDs with matching intent phrases.
    """
    logger.debug("Matching parsed input against Article intents...")
    text = parsed.structured.get("scenario", "").lower()
    matched_articles = []

    for article_id, intent_phrase in ARTICLE_INTENT_DATABASE.items():
        if intent_phrase in text:
            matched_articles.append(article_id)

    success = len(matched_articles) > 0
    return IntentMatchResult(
        matched_articles=matched_articles,
        success=success
    )
