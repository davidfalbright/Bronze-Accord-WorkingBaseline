# ===============================
# Module: bites_injection_point.py
# Purpose: Surface a bite to the user or system layer at the
#          appropriate moment (console, UI, log, memory refresh)
# Part of: Background Insight & Trigger Exposure Scheduler (BITES)
# ===============================

import logging
from framework_models import BiteTask, BiteScheduleResult

logger = logging.getLogger(__name__)

def deliver_bite(task: BiteTask) -> BiteScheduleResult:
    """
    Inject the bite into the current user/system channel.

    Args:
        task (BiteTask): The bite being delivered.

    Returns:
        BiteScheduleResult: Delivery success or failure report.
    """
    try:
        # In a live system, this could post to UI, log, or memory
        logger.info(f"🌱 BITES Delivery — [{task.category.upper()}] {task.title}")
        logger.info(task.content)

        # Record the delivery
        from bites_tracker import record_exposure
        record_exposure(task)

        return BiteScheduleResult(success=True)

    except Exception as e:
        logger.exception("Failed to deliver bite.")
        return BiteScheduleResult(success=False, reason=str(e))