# charter_structure_validator.py

from typing import Dict, List

class CharterStructureValidator:
    """
    Validates the internal structure of the loaded Charter YAML block
    to ensure Convictions, Safeguards, Principles, Articles, and Intents are correctly nested and linked.
    """

    REQUIRED_LAYERS = ["convictions", "safeguards", "principles", "articles"]
    INTENT_FIELDS = ["description", "edge_cases", "rationale"]

    def __init__(self):
        self.errors: List[str] = []

    def validate(self, charter_yaml: Dict) -> bool:
        self.errors.clear()
        for layer in self.REQUIRED_LAYERS:
            if layer not in charter_yaml:
                self.errors.append(f"Missing required layer: '{layer}'")

        if "convictions" in charter_yaml:
            for c_id, c_data in charter_yaml["convictions"].items():
                if "intents" not in c_data:
                    self.errors.append(f"Conviction '{c_id}' missing 'intents'")
                else:
                    self._validate_intents(c_data["intents"], c_id)

        if "articles" in charter_yaml:
            for a_id, a_data in charter_yaml["articles"].items():
                if "intents" not in a_data:
                    self.errors.append(f"Article '{a_id}' missing 'intents'")
                else:
                    self._validate_intents(a_data["intents"], a_id)

        return len(self.errors) == 0

    def _validate_intents(self, intents: List[Dict], parent_id: str):
        for idx, intent in enumerate(intents):
            for field in self.INTENT_FIELDS:
                if field not in intent:
                    self.errors.append(f"Intent {idx} in '{parent_id}' missing field '{field}'")

    def get_errors(self) -> List[str]:
        return self.errors