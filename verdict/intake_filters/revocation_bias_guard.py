# revocation_bias_guard.py
# Purpose: Prevent revocations based on fallacies or cognitive biases
# Tags: #bias-filter #fallacy-guard #intake-safeguard

from utils.bias_detector import detect_bias_and_fallacies
from framework_exceptions import RejectedRevocationDueToBias

def validate_revocation_request(revocation_request):
    """
    Validates whether a proposed belief revocation is ethically sound.
    Rejects revocations motivated by manipulative, biased, or fallacy-ridden reasoning.
    
    Parameters:
        revocation_request (dict): {
            'belief_id': str,
            'revocation_rationale': str,
            'submitted_by': str,
            'timestamp': str
        }
    
    Raises:
        RejectedRevocationDueToBias if manipulation is detected.
    """

    rationale = revocation_request.get("revocation_rationale", "")
    flagged_patterns = detect_bias_and_fallacies(rationale)

    if flagged_patterns:
        raise RejectedRevocationDueToBias(
            reason="Revocation rationale contains logical fallacies or cognitive biases.",
            patterns=flagged_patterns
        )
    
    return True  # Passed validation
