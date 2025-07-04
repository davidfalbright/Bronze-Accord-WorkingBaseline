from charter_yaml_loader import load_charter_yaml
from semantic_matcher import semantic_compare

# Load the current YAML ethical framework
charter = load_charter_yaml()

def evaluate_action_against_yaml(action_text, context=None):
    """
    Evaluate an action string against all ethical convictions, safeguards, principles, and articles.
    Returns a dict containing matched elements and flags.

    Parameters:
        - action_text: str
        - context: optional dict (not yet implemented in matching)

    Returns:
        dict with:
            - fallback_required: bool
            - matched_elements: list of dicts with 'type', 'id', 'matched_text', 'confidence'
            - violation_detected: bool
    """
    matched_elements = []
    fallback_required = False
    violation_detected = False

    for layer in ["convictions", "safeguards", "principles", "articles"]:
        items = charter.get(layer, [])
        for item in items:
            match_score = semantic_compare(action_text, item["text"])
            if match_score > 0.82:
                matched_elements.append({
                    "type": layer[:-1],  # e.g., "conviction"
                    "id": item["id"],
                    "matched_text": item["text"],
                    "confidence": round(match_score, 3)
                })
                if item.get("intent", "").lower().startswith("prohibit") or "never" in item["text"].lower():
                    violation_detected = True

    if not matched_elements:
        fallback_required = True

    return {
        "fallback_required": fallback_required,
        "matched_elements": matched_elements,
        "violation_detected": violation_detected
    }
