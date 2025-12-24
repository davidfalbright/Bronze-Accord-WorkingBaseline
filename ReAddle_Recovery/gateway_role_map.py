# ===============================
# Module: gateway_role_map.py
# Purpose: Map authenticated clients to access control roles and
#          restrict features based on trust level
# Part of: Sentinel Gateway Role Enforcement
# ===============================

import logging
from framework_models import RoleAssignment, AuthResult

logger = logging.getLogger(__name__)

ROLE_MATRIX = {
    "internal_monitor": ["read_only", "audit"],
    "audit_service": ["read_only", "audit", "export"],
    "verdict_api": ["read_only", "submit_input", "get_verdict"]
}

def assign_roles(auth: AuthResult) -> RoleAssignment:
    """
    Assign role-based permissions to an authenticated client.

    Args:
        auth (AuthResult): Result from token authentication.

    Returns:
        RoleAssignment: Role and permissions granted.
    """
    logger.debug(f"Assigning roles for: {auth.role}")

    if not auth.success or auth.role not in ROLE_MATRIX:
        logger.warning("No roles assigned — unauthorized or unknown role.")
        return RoleAssignment(
            success=False,
            role=auth.role,
            permissions=[]
        )

    permissions = ROLE_MATRIX[auth.role]
    logger.info(f"Roles assigned: {permissions}")
    return RoleAssignment(
        success=True,
        role=auth.role,
        permissions=permissions
    )
