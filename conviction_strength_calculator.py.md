# conviction_strength_calculator.py.md

```python
# ===============================
# Module: conviction_strength_calculator.py
# Purpose: Calculate the strength level of a conviction being invoked
#          in the context of an ethical evaluation
# Part of: Ethical Weighting / Scoring Engine
# ===============================

import logging
from framework_models import ParsedInput, ConvictionStrengthScore

logger = logging.getLogger(__name__)

CONVICTION_WEIGHTS = {
    "C1": 95,   # Sanctity of Life
    "C2": 90,   # Prevention of Harm
    "C3": 85,   # Respect for Autonomy
    "C4": 80,   # Justice and Fairness
    "C5": 75,   # Truthfulness and Transparency
    "C6": 70    # Stewardship of Power
}

def calculate_conviction_strength(parsed: ParsedInput) -> ConvictionStrengthScore:
    """
    Analyze parsed input to determine overall ethical conviction strength.

    Args:
        parsed (ParsedInput): Structured ethical input.

    Returns:
        ConvictionStrengthScore: Weighted average of triggered convictions.
    """
    logger.debug("Calculating conviction strength from parsed input...")

    triggered = parsed.structured.get("convictions", [])
    if not triggered:
        return ConvictionStrengthScore(value=0, detail="No convictions detected")

    weights = [CONVICTION_WEIGHTS.get(cid, 50) for cid in triggered]
    avg_score = sum(weights) / len(weights)

    logger.info(f"Conviction strength calculated: {avg_score:.2f}")
    return ConvictionStrengthScore(value=avg_score, detail=f"{len(triggered)} convictions triggered")