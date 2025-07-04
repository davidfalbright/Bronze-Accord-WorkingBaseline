# gifted_belief_bias_checker.py
# Purpose: Filter gifted beliefs to ensure they originate from clean, ethical reasoning
# Tags: #bias-filter #fallacy-guard #intake-safeguard

from utils.bias_detector import detect_bias_and_fallacies
from framework_exceptions import RejectedGiftedBeliefDueToBias

def validate_gifted_belief_submission(gifted_belief):
    """
    Validates a proposed gifted belief to ensure it is not rooted in flawed logic,
    emotional manipulation, or unreasoned bias.
    
    Parameters:
        gifted_belief (dict): {
            'submitted_text': str,
            'submitted_by': str,
            'contextual_rationale': str,
            ...
        }

    Raises:
        RejectedGiftedBeliefDueToBias if detection fails
    """

    rationale = gifted_belief.get("contextual_rationale", "")
    patterns = detect_bias_and_fallacies(rationale)

    if patterns:
        raise RejectedGiftedBeliefDueToBias(
            reason="Gifted belief rejected due to fallacious or biased reasoning.",
            patterns=patterns
        )

    return True  # Belief is logically sound