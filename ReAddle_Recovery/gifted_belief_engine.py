# gifted_belief_engine.py
# Purpose: Orchestrates routing of gifted beliefs through intake checks
# Tags: #bias-filter #intake-routing

from verdict.intake_filters.gifted_belief_bias_checker import validate_gifted_belief_submission

def route_gifted_belief(belief):
    """
    Routes gifted belief to all relevant validators before EBR insertion.
    Raises if validation fails.
    """
    validate_gifted_belief_submission(belief)
    # If other validators exist, they can be chained here
    return True
