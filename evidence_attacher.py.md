# evidence_attacher.py

from typing import List, Dict, Any


class EvidenceAttacher:
    """
    Attaches supporting evidence (such as source rationale, textual justifications, or input excerpts)
    to the final verdict to enhance traceability and transparency.
    """

    def __init__(self):
        pass

    def attach(self, conflict_metadata: Dict[str, Any], triggered_elements: Dict[str, List[str]]) -> List[Dict[str, Any]]:
        """
        Constructs supporting evidence for each triggered component.

        Args:
            conflict_metadata: A dictionary containing metadata (e.g. source text, line numbers, origin).
            triggered_elements: Dict with keys like 'convictions', 'safeguards', etc., each with a list of IDs.

        Returns:
            A list of structured evidence entries.
        """
        evidence_list = []

        for category, ids in triggered_elements.items():
            for eid in ids:
                evidence_list.append({
                    "component_id": eid,
                    "component_type": category,
                    "rationale": f"Triggered due to {conflict_metadata.get('reason', 'unspecified reason')}",
                    "source": conflict_metadata.get("source"),
                    "context": conflict_metadata.get("context", None)
                })

        return evidence_list


# Example usage
if __name__ == "__main__":
    conflict = {
        "source": "Religious Insight Engine",
        "reason": "Violation of non-coercion",
        "context": "Rule X contradicted the autonomy safeguard"
    }
    triggered = {
        "convictions": ["C1"],
        "safeguards": ["S4"],
        "articles": ["A1.2"]
    }

    attacher = EvidenceAttacher()
    print("Evidence:", attacher.attach(conflict, triggered))