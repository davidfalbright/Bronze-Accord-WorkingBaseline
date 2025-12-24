"""
INTERLACE Engine
Compares and reconciles belief bundles across reservoirs using symbolic + semantic logic.
"""

from semantic_conflict_detector import detect_conflict
from semantic_matcher import match_beliefs
from edge_case_reasoning import evaluate_edge_case
from text_similarity_utils import compute_similarity_score

class InterlaceEngine:
    def __init__(self):
        pass

    def reconcile_bundles(self, bundle_a, bundle_b):
        result = {
            "conflicts": detect_conflict(bundle_a, bundle_b),
            "matches": match_beliefs(bundle_a, bundle_b),
            "edge_cases": evaluate_edge_case(bundle_a, bundle_b),
            "similarity_score": compute_similarity_score(bundle_a, bundle_b)
        }
        return result


    def format_input(self, raw_yaml_dict):
        """
        Converts YAML-parsed input into canonical belief bundle format for analysis.
        """
        # Normalize common fields
        return {
            "id": raw_yaml_dict.get("id"),
            "origin": raw_yaml_dict.get("source") or raw_yaml_dict.get("origin"),
            "belief_text": raw_yaml_dict.get("belief") or raw_yaml_dict.get("statement"),
            "tags": raw_yaml_dict.get("tags", []),
            "context": raw_yaml_dict.get("context", "")
        }

    def process_and_reconcile(self, yaml_bundle_a, yaml_bundle_b):
        """
        Applies normalization and then performs full reconciliation.
        """
        bundle_a = self.format_input(yaml_bundle_a)
        bundle_b = self.format_input(yaml_bundle_b)
        return self.reconcile_bundles(bundle_a, bundle_b)

# Example usage:
# engine = InterlaceEngine()
# belief_result = engine.process_and_reconcile(belief_a, belief_b)
