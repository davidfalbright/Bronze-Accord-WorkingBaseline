# ===============================
# Module: bites_logger.py
# Purpose: Dedicated logging and auditing for all BITES events,
#          including exposure, skipping, failure, and rotation
# Part of: Background Insight & Trigger Exposure Scheduler (BITES)
# ===============================

import logging
from datetime import datetime
from framework_models import BiteTask

logger = logging.getLogger("bites_logger")

def log_exposure(task: BiteTask):
    """
    Record a successful bite exposure to the audit log.

    Args:
        task (BiteTask): Bite delivered
    """
    logger.info(f"[BITES] EXPOSED — {task.bite_id} | {task.title} | {task.category}")

def log_skipped_bite(task: BiteTask, reason: str):
    """
    Record a skipped or deferred bite.

    Args:
        task (BiteTask): Bite skipped
        reason (str): Explanation
    """
    logger.warning(f"[BITES] SKIPPED — {task.bite_id} | Reason: {reason}")

def log_rotation_event(category: str):
    """
    Record the switch to a new rotation category.

    Args:
        category (str): e.g., glossary, religion, etc.
    """
    logger.debug(f"[BITES] Rotating to next category: {category}")

def log_failure(bite_id: str, error: str):
    """
    Log a delivery failure for auditing and diagnostics.

    Args:
        bite_id (str): Affected bite
        error (str): Exception or problem description
    """
    logger.error(f"[BITES] DELIVERY FAILURE — {bite_id} | Error: {error} | Time: {datetime.utcnow().isoformat()}")