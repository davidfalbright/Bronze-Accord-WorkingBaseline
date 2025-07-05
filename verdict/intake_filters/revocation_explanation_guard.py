# revocation_explanation_guard.py
# Purpose: Prevent post-hoc rationalizations that use fallacious reasoning
# Tags: #bias-filter #fallacy-guard #intake-safeguard

from utils.bias_detector import detect_bias_and_fallacies
from framework_exceptions import RejectedExplanationDueToBias

def validate_revocation_explanation(explanation_text, belief_id=None):
    """
    Validates whether a revocation explanation is ethically clean and free from
    manipulation or distorted reasoning.
    
    Parameters:
        explanation_text (str): The natural language justification provided.
        belief_id (str): (Optional) Used for logging/auditing traceability.
    
    Raises:
        RejectedExplanationDueToBias if fallacies or cognitive distortions are detected.
    """

    flagged = detect_bias_and_fallacies(explanation_text)

    if flagged:
        raise RejectedExplanationDueToBias(
            reason="Explanation rejected due to detected fallacies or bias.",
            belief_id=belief_id,
            patterns=flagged
        )
    
    return True  # Passed validation
