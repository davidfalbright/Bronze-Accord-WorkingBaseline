# ===============================
# Module: sage_verdict_bridge.py
# Purpose: Bridge SAGE enforcement results into the braid verdict pipeline,
#          allowing symbolic violations to modify or block verdicts
# Part of: SAGELINK Verdict Integration
# ===============================

import logging
from framework_models import EnforcementResult, EngineOutcome, SageBridgeResult, Verdict

logger = logging.getLogger(__name__)

def apply_sage_impact(enforcement: EnforcementResult, prior_outcome: EngineOutcome) -> SageBridgeResult:
    """
    Adjust or override braid verdicts based on symbolic enforcement feedback.

    Args:
        enforcement (EnforcementResult): Result of SAGE enforcement
        prior_outcome (EngineOutcome): Initial verdict outcome

    Returns:
        SageBridgeResult: New outcome if modified, else passthrough
    """
    logger.debug("Applying SAGE impact to verdict...")

    if not enforcement.success and enforcement.violated_rules:
        # Block or adjust verdict due to SAGE violation
        new_verdict = Verdict(
            decision="Block action",
            strength="absolute",
            rationale="SAGE rule violation overrides braid verdict"
        )
        logger.warning("SAGE override: Verdict forcibly blocked.")
        return SageBridgeResult(
            modified=True,
            final_outcome=EngineOutcome(success=True, verdict=new_verdict)
        )

    # No violations — passthrough original
    return SageBridgeResult(modified=False, final_outcome=prior_outcome)