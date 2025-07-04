# ===============================
# Module: bites_tracker.py
# Purpose: Track exposure history for each bite to avoid overuse
#          and ensure meaningful distribution
# Part of: Background Insight & Trigger Exposure Scheduler (BITES)
# ===============================

import logging
from datetime import datetime, timedelta
from typing import Dict, Optional
from framework_models import BiteTask

logger = logging.getLogger(__name__)

# In-memory exposure log: bite_id -> datetime
EXPOSURE_LOG: Dict[str, datetime] = {}

# Time threshold before a bite can be shown again
MIN_INTERVAL = timedelta(days=7)

def record_exposure(task: BiteTask):
    """
    Log that a bite has been shown.

    Args:
        task (BiteTask): The delivered bite task
    """
    logger.info(f"Recording exposure for bite: {task.bite_id}")
    EXPOSURE_LOG[task.bite_id] = datetime.utcnow()

def has_been_exposed_recently(bite_id: str) -> bool:
    """
    Check if the bite was shown too recently.

    Args:
        bite_id (str): Unique identifier

    Returns:
        bool: True if too recent, False if eligible
    """
    last_seen = EXPOSURE_LOG.get(bite_id)
    if not last_seen:
        return False
    return datetime.utcnow() - last_seen < MIN_INTERVAL

def get_next_eligible_bite() -> Optional[BiteTask]:
    """
    Convenience wrapper using the rotation engine to fetch a bite.

    Returns:
        BiteTask or None
    """
    from bites_rotation_engine import get_next_category, select_bite_from_category
    category = get_next_category()
    return select_bite_from_category(category)
