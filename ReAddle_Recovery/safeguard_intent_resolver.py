# safeguard_intent_resolver.py

from typing import List, Dict


class SafeguardIntentResolver:
    """
    Extracts and returns intent text for each Safeguard from the Charter YAML.
    Supports explanation of S-level decisions and alignment checks.
    """

    def __init__(self, charter_data: Dict):
        """
        Args:
            charter_data (Dict): Full parsed Charter YAML content.
        """
        self.intent_map = self._extract_safeguard_intents(charter_data)

    def _extract_safeguard_intents(self, charter_data: Dict) -> Dict[str, str]:
        """
        Builds a map from safeguard ID to their full intent string.

        Returns:
            Dict[str, str]
        """
        results = {}
        for sid, sinfo in charter_data.get("Safeguards", {}).items():
            if "Intents" in sinfo:
                joined = " ".join(sinfo["Intents"])
                results[sid] = joined.strip()
        return results

    def resolve(self, safeguard_ids: List[str]) -> List[str]:
        """
        Returns the intents for given Safeguard codes.

        Args:
            safeguard_ids (List[str])

        Returns:
            List[str]: List of corresponding intent texts
        """
        return [self.intent_map.get(sid, "") for sid in safeguard_ids if sid in self.intent_map]
