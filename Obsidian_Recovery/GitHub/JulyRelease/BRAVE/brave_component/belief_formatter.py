class BeliefFormatter:
    def format(self, ranked_beliefs):
        # Convert to structured response
        return [{"belief_text": b["belief"], "strength": b["conviction_strength"]} for b in ranked_beliefs]