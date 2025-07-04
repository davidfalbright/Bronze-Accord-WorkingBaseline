# ===============================
# Module: bites_rotation_engine.py
# Purpose: Rotate through eligible bite categories (e.g. religion, jargon, glossary)
#          to ensure long-term exposure balance
# Part of: Background Insight & Trigger Exposure Scheduler (BITES)
# ===============================

import logging
from typing import List, Optional
from framework_models import BiteCategory, BiteTask
from bites_registry import get_available_bites
from bites_tracker import has_been_exposed_recently

logger = logging.getLogger(__name__)

CATEGORY_ROTATION_ORDER = [
    "glossary",
    "religion",
    "jargon",
    "charter",
    "history",
    "custom"
]

_current_category_index = 0

def get_next_category() -> str:
    """
    Determine the next bite category in the rotation order.
    """
    global _current_category_index
    category = CATEGORY_ROTATION_ORDER[_current_category_index]
    _current_category_index = (_current_category_index + 1) % len(CATEGORY_ROTATION_ORDER)
    return category

def select_bite_from_category(category: str) -> Optional[BiteTask]:
    """
    Choose the next eligible bite from the current category.

    Args:
        category (str): Category type ("glossary", "religion", etc.)

    Returns:
        BiteTask or None if no eligible bite is found
    """
    logger.debug(f"Selecting bite from category: {category}")
    candidates: List[BiteTask] = get_available_bites(category=category)

    for task in candidates:
        if not has_been_exposed_recently(task.bite_id):
            return task

    logger.info(f"No new bites found in category: {category}")
    return None