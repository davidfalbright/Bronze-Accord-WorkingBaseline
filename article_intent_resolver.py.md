# article_intent_resolver.py

from typing import List, Dict


class ArticleIntentResolver:
    """
    Extracts and maps article-level intents from the YAML Charter definitions.
    This allows nuanced alignment between dilemmas and the Accord’s ethical articles.
    """

    def __init__(self, charter_data: Dict):
        """
        Args:
            charter_data (Dict): Parsed YAML dictionary containing all Charter sections.
        """
        self.article_intents = self._extract_article_intents(charter_data)

    def _extract_article_intents(self, charter_data: Dict) -> Dict[str, str]:
        """
        Extracts article IDs and their corresponding intent text.

        Returns:
            Dict[str, str]: Mapping from Article ID (e.g. A1.3) to its intent summary.
        """
        result = {}
        for article_id, article_info in charter_data.get("Articles", {}).items():
            if "Intents" in article_info:
                intent_texts = [intent for intent in article_info["Intents"] if isinstance(intent, str)]
                result[article_id] = " ".join(intent_texts).strip()
        return result

    def resolve(self, article_ids: List[str]) -> List[str]:
        """
        Retrieves the full intent statements for given article IDs.

        Args:
            article_ids (List[str]): List of article codes (e.g. ["A1.1", "A2.3"])

        Returns:
            List[str]: Corresponding intent descriptions.
        """
        return [self.article_intents.get(aid, "") for aid in article_ids if aid in self.article_intents]