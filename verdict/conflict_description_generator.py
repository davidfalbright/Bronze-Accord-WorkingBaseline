# conflict_description_generator.py

from typing import Dict, Any


class ConflictDescriptionGenerator:
    """
    Generates a natural-language description of the ethical conflict.
    """

    def __init__(self):
        pass

    def generate(self, context: Dict[str, Any], triggered_elements: Dict[str, list]) -> str:
        """
        Builds a human-readable summary of the ethical tension or violation.

        Args:
            context: Dictionary containing dilemma text, metadata, and evaluation parameters.
            triggered_elements: Dictionary of triggered ethical elements, grouped by category.

        Returns:
            A string description summarizing the nature of the conflict.
        """
        dilemma_text = context.get("dilemma_text", "an unspecified dilemma")
        parts = []

        if triggered_elements.get("convictions"):
            parts.append("a violation of core ethical convictions")

        if triggered_elements.get("safeguards"):
            parts.append("breaches of protective safeguards")

        if triggered_elements.get("principles"):
            parts.append("tensions with guiding principles")

        if triggered_elements.get("articles"):
            parts.append("conflicts with specific article intents")

        if not parts:
            parts.append("unspecified ethical concerns")

        summary = "; ".join(parts)
        return f"The situation described involves {summary} in relation to: \"{dilemma_text}\"."


# Example usage
if __name__ == "__main__":
    sample_context = {
        "dilemma_text": "An AI overrides a human decision to prevent harm to another person."
    }

    sample_triggered = {
        "convictions": ["C1"],
        "safeguards": ["S3"],
        "principles": [],
        "articles": []
    }

    generator = ConflictDescriptionGenerator()
    print(generator.generate(sample_context, sample_triggered))
