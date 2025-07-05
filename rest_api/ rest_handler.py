# rest_handler.py.md

```python
# ===============================
# Module: rest_handler.py
# Purpose: Process incoming REST verdict requests, execute interface logic,
#          and return standardized responses
# Part of: REST Interface Logic
# ===============================

import logging
from fastapi import HTTPException
from framework_models import EthicalInput, VerdictContext, VerdictResponse
from verdict_interface import request_verdict

logger = logging.getLogger(__name__)

async def handle_verdict_request(input_data: EthicalInput, context: VerdictContext) -> VerdictResponse:
    """
    Process a verdict request from REST interface.

    Args:
        input_data (EthicalInput): The raw input submitted by the client.
        context (VerdictContext): Additional context for scoring and constraints.

    Returns:
        VerdictResponse: Standardized verdict reply for the client.
    """
    logger.info("Handling REST verdict request...")

    outcome = request_verdict(input_data, context)
    if not outcome.success:
        raise HTTPException(status_code=400, detail=outcome.message)

    return VerdictResponse.from_engine_outcome(outcome)
