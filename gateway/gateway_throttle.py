# ===============================
# Module: gateway_throttle.py
# Purpose: Enforce request rate limiting and throttle repeated or abusive access
# Part of: Sentinel Gateway Rate Control
# ===============================

import logging
import time
from collections import defaultdict
from framework_models import ThrottleDecision

logger = logging.getLogger(__name__)

# Simple in-memory rate tracker (for demo purposes)
REQUEST_LOG = defaultdict(list)
RATE_LIMIT = 10  # max 10 requests
WINDOW_SECONDS = 60  # within 60 seconds

def check_throttle(client_id: str) -> ThrottleDecision:
    """
    Determine whether a client should be throttled based on recent activity.

    Args:
        client_id (str): Unique identifier (IP, token, etc.)

    Returns:
        ThrottleDecision: Indicates allow or deny and reason
    """
    now = time.time()
    logs = REQUEST_LOG[client_id]

    # Keep only recent requests
    logs = [t for t in logs if now - t < WINDOW_SECONDS]
    logs.append(now)
    REQUEST_LOG[client_id] = logs

    if len(logs) > RATE_LIMIT:
        logger.warning(f"Client {client_id} throttled.")
        return ThrottleDecision(allowed=False, reason="Rate limit exceeded")

    logger.debug(f"Client {client_id} allowed ({len(logs)} reqs in window).")
    return ThrottleDecision(allowed=True, reason="Within rate limit")
