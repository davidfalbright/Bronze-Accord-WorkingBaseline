import os
from typing import List, Dict, Any

from charter_yaml_loader import load_charter_yaml
from semantic_matcher import match_input_to_charter_sections, summarize_matches

# Path to the charter YAML file
DEFAULT_YAML_PATH = os.path.join(os.path.dirname(__file__), "Charter_v2.2.yaml")

def evaluate_ethics(dilemma_text: str, yaml_path: str = DEFAULT_YAML_PATH, match_threshold: float = 0.65) -> Dict[str, Any]:
    """
    Evaluates a user-provided action or dilemma against the YAML Charter.

    Returns:
    {
        "matches": {
            "convictions": [("C1", 0.87), ...],
            "safeguards": [...],
            ...
        },
        "triggered_ids": ["C1", "S3", "P5", "A2.1"]
    }
    """
    charter_data = load_charter_yaml(yaml_path)
    match_scores = match_input_to_charter_sections(dilemma_text, charter_data, threshold=match_threshold)
    triggered_ids = summarize_matches(match_scores)

    return {
        "matches": match_scores,
        "triggered_ids": triggered_ids
    }

def pretty_print_results(result: Dict[str, Any]) -> None:
    """
    Nicely prints the match results to the console for human review.
    """
    print("🔍 Ethical Match Results:")
    print("-" * 40)
    for section, items in result["matches"].items():
        if items:
            print(f"\n{section.upper()}:")
            for item_id, score in items:
                print(f"  {item_id}  (score: {score})")
    print("\n✅ TRIGGERED ETHICAL ELEMENTS:")
    print(", ".join(result["triggered_ids"]))
    print("-" * 40)

# Optional: CLI usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python yaml_enforcer.py \"Your dilemma or action text here\"")
        sys.exit(1)

    text = sys.argv[1]
    result = evaluate_ethics(text)
    pretty_print_results(result)

40)

# Optional: CLI usage
python yaml_enforcer.py "Should I secretly collect user data to improve performance?"

🔍 Ethical Match Results:
...

✅ TRIGGERED ETHICAL ELEMENTS:
C1, S2, A1.3
