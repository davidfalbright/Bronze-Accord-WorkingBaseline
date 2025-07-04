# principle_intent_resolver.py

from typing import List, Dict


class PrincipleIntentResolver:
    """
    Extracts and returns intent text for each Principle from the Charter YAML.
    Supports explanation of P-level decisions and alignment checks.
    """

    def __init__(self, charter_data: Dict):
        """
        Args:
            charter_data (Dict): Full parsed Charter YAML content.
        """
        self.intent_map = self._extract_principle_intents(charter_data)

    def _extract_principle_intents(self, charter_data: Dict) -> Dict[str, str]:
        """
        Returns a dictionary mapping Principle IDs to their full intent text.

        Returns:
            Dict[str, str]
        """
        results = {}
        for pid, pinfo in charter_data.get("Principles", {}).items():
            if "Intents" in pinfo:
                joined = " ".join(pinfo["Intents"])
                results[pid] = joined.strip()
        return results

    def resolve(self, principle_ids: List[str]) -> List[str]:
        """
        Returns the intents for given Principle codes.

        Args:
            principle_ids (List[str])

        Returns:
            List[str]: List of corresponding intent texts
        """
        return [self.intent_map.get(pid, "") for pid in principle_ids if pid in self.intent_map]