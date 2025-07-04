# ===============================
# Module: recovery_flag.py
# Purpose: Detect whether the system is recovering from a crash or
#          critical fault, and set internal state accordingly
# Part of: AutoBoot Recovery Layer
# ===============================

import os
import logging
from framework_models import RecoveryStatus

logger = logging.getLogger(__name__)

RECOVERY_FLAG_PATH = "/tmp/braid_recovery.flag"

def check_recovery_flag() -> RecoveryStatus:
    """
    Check if the system is starting in recovery mode.

    Returns:
        RecoveryStatus: Flag state and recommended action.
    """
    logger.debug("Checking for recovery flag...")

    if os.path.exists(RECOVERY_FLAG_PATH):
        logger.warning("Recovery flag detected. System may have crashed previously.")
        return RecoveryStatus(
            recovery_mode=True,
            message="System is restarting in recovery mode."
        )

    return RecoveryStatus(
        recovery_mode=False,
        message="Normal startup"
    )


def set_recovery_flag():
    """
    Write recovery flag to disk.
    """
    with open(RECOVERY_FLAG_PATH, "w") as f:
        f.write("RECOVERY_MODE=1")
    logger.info("Recovery flag set.")


def clear_recovery_flag():
    """
    Remove recovery flag if present.
    """
    if os.path.exists(RECOVERY_FLAG_PATH):
        os.remove(RECOVERY_FLAG_PATH)
        logger.info("Recovery flag cleared.")
