# ===============================
# Module: gateway_bridge.py
# Purpose: Act as a secure relay between the Gateway and other subsystems,
#          coordinating handoff of authenticated and filtered requests
# Part of: Sentinel Gateway Integration Layer
# ===============================

import logging
from framework_models import GatewayRequest, VerdictContext, GatewayBridgeResult
from verdict_interface import request_verdict

logger = logging.getLogger(__name__)

def forward_request_to_verdict_engine(request: GatewayRequest) -> GatewayBridgeResult:
    """
    Relay a validated request to the verdict interface.

    Args:
        request (GatewayRequest): Already authenticated, filtered, and decoded

    Returns:
        GatewayBridgeResult: Verdict or error, ready for Gateway Response
    """
    logger.info(f"Relaying request from source: {request.source_id}")

    try:
        input_data = request.payload
        context = VerdictContext(
            allow_fallbacks=True,
            use_compression=True,
            override_mode=None
        )

        outcome = request_verdict(input_data, context)
        return GatewayBridgeResult(success=True, outcome=outcome)

    except Exception as e:
        logger.exception("Failed to relay request to verdict engine.")
        return GatewayBridgeResult(success=False, message=str(e))
