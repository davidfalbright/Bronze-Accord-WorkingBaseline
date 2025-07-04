# ===============================
# Module: rest_test_endpoint.py
# Purpose: Provide a sandbox endpoint for internal testing, integration checks,
#          or mock input submission
# Part of: REST Test Suite Interface
# ===============================

from fastapi import APIRouter
from framework_models import TestPayload, TestResult

router = APIRouter()

@router.post("/api/test/echo", response_model=TestResult)
async def test_echo(payload: TestPayload):
    """
    Echo back test payload to validate routing and deserialization.

    Args:
        payload (TestPayload): Simple input for testing.

    Returns:
        TestResult: Echoed input and confirmation.
    """
    return TestResult(
        received=payload.message,
        confirmed=True
    )