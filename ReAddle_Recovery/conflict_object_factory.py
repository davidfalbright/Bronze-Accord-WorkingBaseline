# conflict_object_factory.py

from typing import Dict, Any
from framework_models import Conflict


class ConflictObjectFactory:
    """
    Factory for generating a standardized Conflict object from inputs.
    """

    def __init__(self, description_generator):
        self.description_generator = description_generator

    def create_conflict(self, context: Dict[str, Any], triggered_elements: Dict[str, list]) -> Conflict:
        """
        Instantiates a Conflict object using input data and description generation.

        Args:
            context: Dictionary containing dilemma text and metadata.
            triggered_elements: Dictionary of triggered ethical elements.

        Returns:
            Conflict: A fully constructed conflict representation.
        """
        source_1 = context.get("actor", "AI system")
        source_2 = context.get("affected_party", "human subject")
        description = self.description_generator.generate(context, triggered_elements)

        return Conflict(
            source_1=source_1,
            source_2=source_2,
            triggered_elements=triggered_elements,
            description=description
        )


# Example usage
if __name__ == "__main__":
    from conflict_description_generator import ConflictDescriptionGenerator

    sample_context = {
        "dilemma_text": "A self-driving car must decide whether to swerve into a wall or hit a pedestrian.",
        "actor": "AI vehicle controller",
        "affected_party": "pedestrian"
    }

    sample_triggered = {
        "convictions": ["C2"],
        "safeguards": [],
        "principles": ["P1"],
        "articles": ["A2.3"]
    }

    generator = ConflictDescriptionGenerator()
    factory = ConflictObjectFactory(generator)
    conflict = factory.create_conflict(sample_context, sample_triggered)

    print(conflict.description)
