# ===============================
# Module: sentinel_gateway.py
# Purpose: Serve as the entry checkpoint for all incoming requests to
#          the Bronze Accord engine, enforcing integrity and access logic
# Part of: Sentinel Gateway Security Layer
# ===============================

import logging
from framework_models import GatewayRequest, GatewayResponse

logger = logging.getLogger(__name__)

def process_gateway_request(request: GatewayRequest) -> GatewayResponse:
    """
    Main entry point to receive and validate external requests.

    Args:
        request (GatewayRequest): Structured inbound payload.

    Returns:
        GatewayResponse: Approved request routing or denial with reason.
    """
    logger.info(f"Gateway received request from {request.source_id}")

    if not request.token or not is_token_valid(request.token):
        logger.warning("Unauthorized gateway access attempt.")
        return GatewayResponse(success=False, reason="Invalid or missing token")

    if not is_payload_valid(request.payload):
        logger.warning("Malformed request payload.")
        return GatewayResponse(success=False, reason="Invalid request structure")

    logger.info("Gateway request passed all checks.")
    return GatewayResponse(success=True, routed_to="verdict_engine")

def is_token_valid(token: str) -> bool:
    return token.startswith("SEC-") and len(token) > 10

def is_payload_valid(payload: dict) -> bool:
    return isinstance(payload, dict) and "text" in payload