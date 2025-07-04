# contextual_conflict_extractor.py

from framework_models import EthicalContext, ConflictAlert

class ContextualConflictExtractor:
    def __init__(self, principles, convictions, safeguards):
        self.principles = principles
        self.convictions = convictions
        self.safeguards = safeguards

    def extract_conflicts(self, context: EthicalContext):
        """
        Identifies ethical tensions arising from conflicting activated elements.
        Returns a list of ConflictAlert instances.
        """
        active_principles = context.get_active_principles()
        active_safeguards = context.get_active_safeguards()
        active_convictions = context.get_active_convictions()

        alerts = []

        # Example conflict: Principle vs Safeguard
        for p in active_principles:
            for s in active_safeguards:
                if p.overlaps_negatively_with(s):
                    alerts.append(ConflictAlert(
                        type="Principle vs Safeguard",
                        source_1=p.id,
                        source_2=s.id,
                        description=f"{p.name} may override {s.name} in current context.",
                        severity="moderate"
                    ))

        # Conflict: Conviction override logic
        for c in active_convictions:
            for p in active_principles:
                if c.supersedes(p):
                    alerts.append(ConflictAlert(
                        type="Conviction over Principle",
                        source_1=c.id,
                        source_2=p.id,
                        description=f"Conviction {c.name} supersedes Principle {p.name}.",
                        severity="high"
                    ))

        # Future: Cross-layer conflicts and historical paradox detection

        return alerts