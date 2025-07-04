# verdict_conflict_object.py

from typing import List, Dict


class ConflictInstance:
    """
    Represents a specific ethical conflict between two belief sources.
    """

    def __init__(self, source_1: str, source_2: str, triggered_elements: Dict[str, List[str]], description: str):
        self.source_1 = source_1
        self.source_2 = source_2
        self.triggered_elements = triggered_elements  # e.g., {"convictions": ["C1"], "safeguards": ["S3"]}
        self.description = description