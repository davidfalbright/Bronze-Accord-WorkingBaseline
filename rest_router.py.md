# rest_router.py.md

```python
# ===============================
# Module: rest_router.py
# Purpose: Define REST API endpoints and route requests to appropriate
#          handler functions
# Part of: REST Interface Layer
# ===============================

from fastapi import APIRouter
from rest_handler import handle_verdict_request
from framework_models import EthicalInput, VerdictResponse, VerdictContext

router = APIRouter()

@router.post("/api/verdict", response_model=VerdictResponse)
async def verdict_endpoint(input_data: EthicalInput, context: VerdictContext):
    """
    REST endpoint for verdict requests.

    Args:
        input_data (EthicalInput): Input data from the client
        context (VerdictContext): Context object with override options

    Returns:
        VerdictResponse: Final response from the verdict system
    """
    return await handle_verdict_request(input_data, context)