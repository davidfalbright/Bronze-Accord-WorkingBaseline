# semantic_conflict_detector.py

from typing import Dict, List, Tuple


class SemanticConflictDetector:
    """
    Detects internal semantic conflicts between triggered ethical components.
    For example: when one safeguard implies 'halt' but another suggests 'proceed'.
    """

    def __init__(self):
        pass

    def detect_conflicts(
        self, triggered_components: List[str], verdicts: Dict[str, str]
    ) -> Tuple[bool, List[Tuple[str, str]]]:
        """
        Check for contradictions in verdicts tied to different components.

        Returns:
            - conflict_found (bool)
            - conflict_pairs (list of (component, verdict)) entries in conflict
        """
        verdict_map = {}
        for component in triggered_components:
            v = verdicts.get(component)
            if v:
                if v not in verdict_map:
                    verdict_map[v] = []
                verdict_map[v].append(component)

        if len(verdict_map) > 1:
            # Multiple verdicts exist across components = conflict
            conflict_pairs = [
                (component, v)
                for v, components in verdict_map.items()
                for component in components
            ]
            return True, conflict_pairs

        return False, []

    def summarize_conflict(self, conflicts: List[Tuple[str, str]]) -> str:
        """
        Generate a readable summary of the semantic conflict.
        """
        summary = "Semantic conflict detected between the following components:\n"
        for comp, verdict in conflicts:
            summary += f" - {comp} suggests: {verdict}\n"
        return summary