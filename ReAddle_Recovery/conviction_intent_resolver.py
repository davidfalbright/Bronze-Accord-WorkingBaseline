# conviction_intent_resolver.py

from typing import List, Dict


class ConvictionIntentResolver:
    """
    Extracts and returns intent text for each Conviction from the Charter YAML.
    Enables traceable evaluation and explanation of C-level decisions.
    """

    def __init__(self, charter_data: Dict):
        """
        Args:
            charter_data (Dict): Full parsed Charter YAML content.
        """
        self.intent_map = self._extract_conviction_intents(charter_data)

    def _extract_conviction_intents(self, charter_data: Dict) -> Dict[str, str]:
        """
        Returns a dictionary mapping Conviction IDs to their full intent text.

        Returns:
            Dict[str, str]
        """
        results = {}
        for conviction_id, conviction_info in charter_data.get("Convictions", {}).items():
            if "Intents" in conviction_info:
                joined = " ".join(conviction_info["Intents"])
                results[conviction_id] = joined.strip()
        return results

    def resolve(self, conviction_ids: List[str]) -> List[str]:
        """
        Returns the intents for given Conviction codes.

        Args:
            conviction_ids (List[str])

        Returns:
            List[str]: List of corresponding intent texts
        """
        return [self.intent_map.get(cid, "") for cid in conviction_ids if cid in self.intent_map]
