# verdict_interface.py.md

```python
# ===============================
# Module: verdict_interface.py
# Purpose: Expose the verdict engine to other components (e.g., REST, test harness),
#          translating raw user inputs into structured verdict requests
# Part of: Verdict Engine Interface Layer
# ===============================

import logging
from framework_models import EthicalInput, VerdictContext, EngineOutcome
from braid_parser import parse_input
from verdict_engine import generate_verdict

logger = logging.getLogger(__name__)

def request_verdict(input_data: EthicalInput, context: VerdictContext) -> EngineOutcome:
    """
    High-level interface to process an ethical input and return a verdict.

    Args:
        input_data (EthicalInput): The raw ethical dilemma or query.
        context (VerdictContext): Evaluation settings, constraints, overrides.

    Returns:
        EngineOutcome: The result from the verdict engine, including any errors.
    """
    logger.debug("Starting verdict interface flow...")

    parse_result = parse_input(input_data)
    if not parse_result.success:
        return EngineOutcome(success=False, message=f"Parsing failed: {parse_result.message}")

    return generate_verdict(parse_result.parsed, context)
