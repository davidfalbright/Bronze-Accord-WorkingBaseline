# ===============================
# Module: rest_healthcheck.py
# Purpose: Expose system-level readiness and health indicators
#          for infrastructure monitoring
# Part of: REST Interface Utilities
# ===============================

from fastapi import APIRouter
from framework_models import HealthcheckStatus

router = APIRouter()

@router.get("/api/health", response_model=HealthcheckStatus)
async def healthcheck():
    """
    Basic healthcheck endpoint for system monitoring.

    Returns:
        HealthcheckStatus: Simple heartbeat + status flags.
    """
    return HealthcheckStatus(
        status="online",
        braid_ready=True,
        fallback_ready=True,
        memory_usage="stable"
    )
