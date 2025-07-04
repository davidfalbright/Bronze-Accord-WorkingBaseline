# belief_context_enricher.py

from typing import Dict, List

class BeliefContextEnricher:
    """
    Adds contextual metadata to beliefs during ethical reasoning to support traceability,
    historical context, translation caveats, or comparative frameworks.
    """

    def __init__(self):
        self.context_data: Dict[str, Dict] = {}

    def enrich_belief(
        self,
        belief_id: str,
        historical_context: str = "",
        ethical_classification: str = "",
        related_beliefs: List[str] = None,
        doctrinal_weight: str = "",
        origin_tags: List[str] = None
    ):
        self.context_data[belief_id] = {
            "historical_context": historical_context,
            "ethical_classification": ethical_classification,
            "related_beliefs": related_beliefs or [],
            "doctrinal_weight": doctrinal_weight,
            "origin_tags": origin_tags or []
        }

    def get_context(self, belief_id: str) -> Dict:
        return self.context_data.get(belief_id, {})

    def list_all_contexts(self) -> List[Dict]:
        return list(self.context_data.values())

    def reset(self):
        self.context_data.clear()