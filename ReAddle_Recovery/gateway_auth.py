# ===============================
# Module: gateway_auth.py
# Purpose: Authenticate API keys, tokens, or caller identities used to
#          access braid or REST interfaces
# Part of: Sentinel Gateway Security Layer
# ===============================

import logging
from typing import Optional
from framework_models import AuthToken, AuthResult

logger = logging.getLogger(__name__)

AUTHORIZED_KEYS = {
    "SEC-TRUSTED-001": "internal_monitor",
    "SEC-AUDITOR-004": "audit_service",
    "SEC-VERDICT-CORE": "verdict_api"
}

def authenticate_token(token: AuthToken) -> AuthResult:
    """
    Validate an incoming authentication token.

    Args:
        token (AuthToken): Object containing token string and optional metadata.

    Returns:
        AuthResult: Authentication outcome and assigned role.
    """
    logger.debug(f"Authenticating token: {token.value}")

    if token.value in AUTHORIZED_KEYS:
        role = AUTHORIZED_KEYS[token.value]
        logger.info(f"Token authenticated successfully for role: {role}")
        return AuthResult(success=True, role=role)

    logger.warning("Authentication failed: unknown token.")
    return AuthResult(success=False, role=None)
