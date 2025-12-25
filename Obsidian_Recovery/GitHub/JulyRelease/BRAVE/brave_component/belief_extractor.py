class BeliefExtractor:
    def extract(self, tagged):
        # Extract relevant beliefs (simulated here)
        if "belief" in tagged["tags"]:
            return [{"belief": "Protect life", "intent": "Preserve sentient life"}]
        return []