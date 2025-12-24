# duplicate_detector.py

from typing import Dict, List, Tuple

class DuplicateDetector:
    """
    Scans a Charter YAML structure to identify duplicate IDs, phrases, or overly similar entries
    among convictions, safeguards, principles, and articles.
    """

    def __init__(self):
        self.duplicates: List[str] = []

    def detect(self, charter_yaml: Dict) -> List[str]:
        self.duplicates.clear()
        seen_ids = set()
        seen_phrases = set()

        for layer_name in ["convictions", "safeguards", "principles", "articles"]:
            layer = charter_yaml.get(layer_name, {})
            for item_id, item_data in layer.items():
                if item_id in seen_ids:
                    self.duplicates.append(f"Duplicate ID found in {layer_name}: '{item_id}'")
                seen_ids.add(item_id)

                phrase = item_data.get("text", "").strip().lower()
                if phrase in seen_phrases:
                    self.duplicates.append(f"Duplicate phrase in {layer_name}: '{item_data.get('text', '')}'")
                seen_phrases.add(phrase)

        return self.duplicates

    def get_duplicates(self) -> List[str]:
        return self.duplicates
