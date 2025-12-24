# verdict_conflict_object.py

from typing import Dict, List


class ConflictInstance:
    """
    Represents a single ethical conflict scenario.
    """

    def __init__(
        self,
        source_1: str,
        source_2: str,
        triggered_elements: Dict[str, List[str]],
        description: str
    ):
        """
        Args:
            source_1 (str): First source of the ethical input (e.g., user intent, action).
            source_2 (str): Second source causing the conflict (e.g., rule, opposing action).
            triggered_elements (dict): Map from element category (e.g., convictions) to list of triggered IDs.
            description (str): Human-readable description of the conflict.
        """
        self.source_1 = source_1
        self.source_2 = source_2
        self.triggered_elements = triggered_elements
        self.description = description
