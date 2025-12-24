# dilemma_submission_validator.py
# Purpose: Ensure dilemmas are framed ethically and rationally
# Tags: #bias-filter #fallacy-guard

from utils.bias_detector import detect_bias_and_fallacies
from framework_exceptions import RejectedDilemmaDueToBias

def validate_dilemma_submission(submission):
    """
    Validates submitted dilemmas against logical and ethical standards.
    Parameters:
        submission (dict): Must include 'dilemma_text'
    Raises:
        RejectedDilemmaDueToBias if manipulation or bias detected.
    """
    text = submission.get("dilemma_text", "")
    patterns = detect_bias_and_fallacies(text)
    if patterns:
        raise RejectedDilemmaDueToBias(
            reason="Dilemma framing contains cognitive bias or fallacious logic.",
            patterns=patterns
        )
    return True
