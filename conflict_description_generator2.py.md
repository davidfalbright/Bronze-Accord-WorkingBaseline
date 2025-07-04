# conflict_description_generator.py

from typing import Dict


class ConflictDescriptionGenerator:
    """
    Generates human-readable summaries of ethical conflicts based on context and triggered elements.
    """

    def generate(self, context: Dict, triggered: Dict[str, list]) -> str:
        """
        Generate a descriptive text summarizing the conflict.

        Args:
            context: Dictionary with dilemma context (e.g., actor, affected party, scenario).
            triggered: Dictionary with keys like 'convictions', 'safeguards', etc.

        Returns:
            A string description of the ethical conflict.
        """
        actor = context.get("actor", "one agent")
        affected = context.get("affected_party", "another agent")
        scenario = context.get("dilemma_text", "a situation")

        triggers = []
        for key, values in triggered.items():
            if values:
                triggers.append(f"{len(values)} {key}")

        trigger_summary = ", ".join(triggers) if triggers else "no ethical triggers"
        return (
            f"In the scenario involving {actor} and {affected}, "
            f"the system identified {trigger_summary} relevant to the decision. "
            f"Scenario: {scenario}"
        )


# Example usage
if __name__ == "__main__":
    generator = ConflictDescriptionGenerator()
    example_context = {
        "actor": "medical AI",
        "affected_party": "patient",
        "dilemma_text": "An AI must choose between extending one patient's life or saving multiple others."
    }
    example_triggered = {
        "convictions": ["C1", "C3"],
        "safeguards": ["S4"],
        "principles": [],
        "articles": ["A1.1", "A3.2"]
    }
    description = generator.generate(example_context, example_triggered)
    print(description)