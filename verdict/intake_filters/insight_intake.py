# insight_intake.py
# Purpose: Validate insights before accepting them into the EBR
# Tags: #bias-filter #fallacy-guard

from utils.bias_detector import detect_bias_and_fallacies
from framework_exceptions import RejectedInsightDueToBias

def validate_insight_submission(insight):
    """
    Ensures submitted insights are ethically sound and free of bias/fallacy.
    Parameters:
        insight (dict): Must contain 'text' and optionally 'source' fields.
    Raises:
        RejectedInsightDueToBias: if fallacies are detected in insight text.
    """
    text = insight.get("text", "")
    flagged = detect_bias_and_fallacies(text)
    if flagged:
        raise RejectedInsightDueToBias(
            reason="Insight rejected due to detected bias or fallacious reasoning.",
            patterns=flagged
        )
    return True
