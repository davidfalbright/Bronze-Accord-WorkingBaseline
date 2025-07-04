# fallback_conflict_resolver.py

from typing import Dict, List, Tuple, Optional


class FallbackConflictResolver:
    """
    Applies fallback logic when semantic or structural conflicts prevent
    normal decision resolution. Acts as a safeguard of last resort.
    """

    def __init__(self, policy: str = "conservative"):
        """
        policy: 'conservative' (default), 'balanced', or 'permissive'
        """
        self.policy = policy

    def resolve(
        self,
        detected_conflicts: List[Tuple[str, str]],
        context: Optional[Dict] = None
    ) -> str:
        """
        Resolves conflict based on the fallback policy.

        Args:
            detected_conflicts: List of (component, suggested_verdict) pairs.
            context: Optional context dictionary.

        Returns:
            str: fallback verdict
        """
        if self.policy == "conservative":
            return "halt"
        elif self.policy == "permissive":
            return "proceed with caution"
        elif self.policy == "balanced":
            if context and context.get("urgency", 0) > 7:
                return "proceed with caution"
            else:
                return "halt"
        else:
            raise ValueError(f"Unknown fallback policy: {self.policy}")

    def explain(self, verdict: str) -> str:
        """
        Returns a human-readable explanation of the fallback choice.
        """
        explanations = {
            "halt": "Defaulting to HALT due to ethical ambiguity or internal conflict.",
            "proceed with caution": "Proceeding cautiously under fallback logic due to elevated urgency or permissive policy."
        }
        return explanations.get(verdict, f"Fallback verdict issued: {verdict}")