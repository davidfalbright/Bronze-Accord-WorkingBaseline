# context_extractor.py

from typing import Dict


class ContextExtractor:
    """
    Extracts relevant dilemma context for ethical evaluation.
    """

    def extract(self, dilemma: Dict) -> Dict:
        """
        Extracts key actors and situation details from a dilemma dictionary.

        Args:
            dilemma: Dictionary with at least the keys 'dilemma_text', 'metadata', etc.

        Returns:
            A dictionary containing:
                - actor
                - affected_party
                - dilemma_text
        """
        # Default fallbacks
        default_actor = "unspecified agent"
        default_affected = "unspecified party"

        # Simple metadata extraction pattern
        metadata = dilemma.get("metadata", {})
        actor = metadata.get("actor", default_actor)
        affected = metadata.get("affected_party", default_affected)
        text = dilemma.get("dilemma_text", "[No dilemma provided]")

        return {
            "actor": actor,
            "affected_party": affected,
            "dilemma_text": text
        }


# Example usage
if __name__ == "__main__":
    extractor = ContextExtractor()
    sample_dilemma = {
        "dilemma_text": "A robot must decide whether to report a factory violation or protect its employer.",
        "metadata": {
            "actor": "industrial robot",
            "affected_party": "employer"
        }
    }
    context = extractor.extract(sample_dilemma)
    print(context)