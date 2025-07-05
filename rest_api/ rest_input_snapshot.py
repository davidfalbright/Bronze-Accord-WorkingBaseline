# ===============================
# Module: rest_input_snapshot.py
# Purpose: Capture and store a snapshot of a user's ethical input
#          for traceability and offline analysis
# Part of: REST Input Logging Tools
# ===============================

import logging
from datetime import datetime
from framework_models import EthicalInput, SnapshotReceipt

logger = logging.getLogger(__name__)
SNAPSHOT_LOG = []

def store_input_snapshot(input_data: EthicalInput) -> SnapshotReceipt:
    """
    Store a snapshot of the input data with timestamp.

    Args:
        input_data (EthicalInput): The user's ethical query.

    Returns:
        SnapshotReceipt: Confirmation with ID and timestamp.
    """
    timestamp = datetime.utcnow().isoformat()
    entry = {
        "timestamp": timestamp,
        "input": input_data.text,
        "metadata": input_data.metadata or {}
    }

    SNAPSHOT_LOG.append(entry)
    logger.info(f"Stored input snapshot at {timestamp}")

    return SnapshotReceipt(
        timestamp=timestamp,
        snapshot_id=f"snap-{len(SNAPSHOT_LOG)}"
    )
