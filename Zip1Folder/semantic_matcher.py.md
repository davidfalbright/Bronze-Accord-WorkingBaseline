import difflib
from typing import List, Tuple, Dict

def fuzzy_match_score(text_a: str, text_b: str) -> float:
    """
    Returns a fuzzy similarity ratio between two strings using difflib.
    Output range: 0.0 to 1.0
    """
    return difflib.SequenceMatcher(None, text_a.lower(), text_b.lower()).ratio()

def match_input_to_charter_sections(input_text: str, charter_data: Dict, threshold: float = 0.65) -> Dict[str, List[Tuple[str, float]]]:
    """
    Compares input_text to each section of the charter (convictions, safeguards, principles, articles)
    using fuzzy matching.

    Returns a dictionary of matches above the threshold:
    {
        "convictions": [("C1", 0.88), ("C4", 0.74)],
        "safeguards": [("S2", 0.71)],
        ...
    }
    """
    matches = {}

    for section in ["convictions", "safeguards", "principles", "articles"]:
        section_matches = []
        for item in charter_data.get(section, []):
            score = fuzzy_match_score(input_text, item["text"])
            if score >= threshold:
                section_matches.append((item["id"], round(score, 3)))
        matches[section] = sorted(section_matches, key=lambda x: x[1], reverse=True)

    return matches

def summarize_matches(matches: Dict[str, List[Tuple[str, float]]]) -> List[str]:
    """
    Converts match dictionary to a simple list of IDs, sorted by section priority.

    Example output:
        ["C1", "C4", "S2"]
    """
    result = []
    for section in ["convictions", "safeguards", "principles", "articles"]:
        result.extend([match[0] for match in matches.get(section, [])])
    return result