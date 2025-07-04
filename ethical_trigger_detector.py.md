# ethical_trigger_detector.py

from typing import Dict, List, Any


class EthicalTriggerDetector:
    """
    Determines which ethical components are activated based on dilemma content.
    """

    def __init__(self, yaml_structure: Dict[str, Any]):
        self.yaml_data = yaml_structure

    def match_keywords(self, text: str, keywords: List[str]) -> bool:
        """
        Checks if any of the provided keywords appear in the input text.
        """
        return any(kw.lower() in text.lower() for kw in keywords)

    def detect_triggers(self, dilemma_text: str) -> Dict[str, List[str]]:
        """
        Scans the dilemma text and identifies all applicable Convictions, Safeguards,
        Principles, and Articles based on keyword matching.
        Returns a dictionary of the form:
            {
                "convictions": ["C1", "C3"],
                "safeguards": ["S1"],
                "principles": ["P1"],
                "articles": ["A1.2"]
            }
        """
        result = {"convictions": [], "safeguards": [], "principles": [], "articles": []}

        for layer in result.keys():
            for item in self.yaml_data.get(layer, {}):
                keywords = self.yaml_data[layer][item].get("keywords", [])
                if self.match_keywords(dilemma_text, keywords):
                    result[layer].append(item)

        return result


# Example usage
if __name__ == "__main__":
    dummy_yaml = {
        "convictions": {
            "C1": {"keywords": ["harm", "injury", "violence"]},
            "C3": {"keywords": ["consent", "permission", "agree"]}
        },
        "safeguards": {
            "S1": {"keywords": ["override", "fail-safe"]}
        },
        "principles": {
            "P1": {"keywords": ["truth", "honesty"]}
        },
        "articles": {
            "A1.2": {"keywords": ["bias", "fairness"]}
        }
    }

    detector = EthicalTriggerDetector(dummy_yaml)
    sample_text = "This action could cause harm and requires explicit consent."
    hits = detector.detect_triggers(sample_text)
    print("Triggered:", hits)