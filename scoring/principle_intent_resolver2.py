# principle_intent_resolver.py

from framework_models import Principle, Intent
from shared_intent_utility import resolve_conflict_between_intents

class PrincipleIntentResolver:
    def __init__(self, principle_registry):
        self.principles = principle_registry  # Dictionary: {principle_id: Principle}

    def get_intents_for_principle(self, principle_id):
        principle = self.principles.get(principle_id)
        if not principle:
            raise ValueError(f"Principle '{principle_id}' not found in registry.")
        return principle.intents

    def evaluate_principle_with_context(self, principle_id, context):
        """
        Evaluates a principle's intents against a given context.
        Returns a structured interpretation, including whether the principle affirms, opposes, or qualifies the proposed action.
        """
        intents = self.get_intents_for_principle(principle_id)
        evaluations = []
        for intent in intents:
            result = intent.evaluate(context)
            evaluations.append({
                "intent_id": intent.id,
                "outcome": result.outcome,
                "confidence": result.confidence,
                "rationale": result.rationale
            })
        return evaluations

    def resolve_conflicting_principles(self, principle_ids, context):
        """
        Compares multiple principles and their intents, returning a reconciled recommendation.
        """
        all_evaluations = {
            pid: self.evaluate_principle_with_context(pid, context) for pid in principle_ids
        }

        # Flatten and collect all intents for conflict resolution
        intents_grouped = [intent for evals in all_evaluations.values() for intent in evals]
        resolved_result = resolve_conflict_between_intents(intents_grouped)
        return resolved_result
