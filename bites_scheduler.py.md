# ===============================
# Module: bites_scheduler.py
# Purpose: Central BITES orchestrator — determines which insight
#          or learning artifact to surface based on timing and context
# Part of: Background Insight & Trigger Exposure Scheduler (BITES)
# ===============================

import logging
import time
from datetime import datetime
from framework_models import BiteTask, BiteScheduleResult
from bites_tracker import get_next_eligible_bite
from bites_injection_point import deliver_bite

logger = logging.getLogger(__name__)
SCHEDULING_INTERVAL_SECONDS = 3600  # Default: 1 hour

def run_bites_scheduler():
    """
    Main loop for running BITES exposure on a timer.
    Can be embedded in a long-lived system loop.
    """
    logger.info("BITES scheduler started.")

    while True:
        task = get_next_eligible_bite()
        if task:
            logger.info(f"Delivering scheduled bite: {task.bite_id}")
            result = deliver_bite(task)
            if not result.success:
                logger.warning(f"Delivery failed: {result.reason}")
        else:
            logger.info("No eligible bites to deliver this cycle.")

        time.sleep(SCHEDULING_INTERVAL_SECONDS)