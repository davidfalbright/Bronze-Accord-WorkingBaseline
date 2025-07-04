# ===============================
# Module: rest_audit_log.py
# Purpose: Record API access logs, inputs, and outcomes for post-hoc review
# Part of: REST Compliance & Audit Trail System
# ===============================

import logging
from datetime import datetime
from framework_models import GatewayRequest, EngineOutcome, AuditLogEntry

logger = logging.getLogger(__name__)
AUDIT_LOG = []

def log_api_interaction(request: GatewayRequest, outcome: EngineOutcome):
    """
    Record a structured audit entry for an incoming API request.

    Args:
        request (GatewayRequest): Inbound request metadata
        outcome (EngineOutcome): Final result of verdict processing
    """
    entry = AuditLogEntry(
        timestamp=datetime.utcnow().isoformat(),
        source=request.source_id,
        decision=outcome.verdict.decision if outcome.success else "N/A",
        success=outcome.success,
        rationale=outcome.verdict.rationale if outcome.success else outcome.message,
    )

    AUDIT_LOG.append(entry)
    logger.info(f"AUDIT LOG: {entry}")