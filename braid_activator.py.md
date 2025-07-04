# braid_activator.py.md

```python
# ===============================
# Module: braid_activator.py
# Purpose: Activate core braid modules in proper dependency order
#          and verify readiness before AI verdict operations begin
# Part of: braid Core Activation Framework
# ===============================

import logging
from braid_core import initialize_core_logic
from braid_parser import verify_parsers
from braid_validator import check_validator_integrity
from framework_models import ActivationStatus

logger = logging.getLogger(__name__)

def activate_braid_stack() -> ActivationStatus:
    """
    Initialize and verify the full braid subsystem.

    Returns:
        ActivationStatus: Result including readiness state and error message if any.
    """
    logger.info("Activating braid system stack...")

    try:
        if not initialize_core_logic():
            return ActivationStatus(success=False, message="Core logic failed to initialize.")

        if not verify_parsers():
            return ActivationStatus(success=False, message="Parser subsystem failed verification.")

        if not check_validator_integrity():
            return ActivationStatus(success=False, message="Validator integrity check failed.")

        logger.info("braid stack successfully activated.")
        return ActivationStatus(success=True, message="braid activation complete.")

    except Exception as e:
        logger.exception("braid activation encountered an error.")
        return ActivationStatus(success=False, message=str(e))