# revocation_router.py
# Purpose: Routes revocation requests through all appropriate guards
# Tags: #bias-filter #intake-routing

from verdict.intake_filters.revocation_bias_guard import validate_revocation_request
from verdict.intake_filters.revocation_explanation_guard import validate_revocation_explanation

def route_revocation_submission(revocation):
    """
    Validates a revocation request and its explanation for ethical compliance.
    """
    validate_revocation_request(revocation)
    explanation = revocation.get("revocation_rationale", "")
    belief_id = revocation.get("belief_id", None)
    validate_revocation_explanation(explanation, belief_id=belief_id)
    return True
