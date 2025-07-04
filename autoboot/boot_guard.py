# ===============================
# Module: boot_guard.py
# Purpose: Prevent system startup if critical conditions are unmet,
#          such as missing models, memory lockout, or prior crash flags
# Part of: AutoBoot Safety Layer
# ===============================

import logging
from framework_models import BootStatus

logger = logging.getLogger(__name__)

REQUIRED_COMPONENTS = ["braid_core", "framework_model_base", "verdict_engine"]

def run_boot_guard() -> BootStatus:
    """
    Perform boot-time safety checks to validate system readiness.

    Returns:
        BootStatus: Pass/fail and summary of missing or broken components.
    """
    logger.info("Running boot guard checks...")
    missing = []

    for component in REQUIRED_COMPONENTS:
        try:
            __import__(component)
        except ImportError:
            logger.warning(f"Missing required module: {component}")
            missing.append(component)

    if missing:
        return BootStatus(success=False, missing_components=missing)

    logger.info("Boot guard passed — all components present.")
    return BootStatus(success=True, missing_components=[])
