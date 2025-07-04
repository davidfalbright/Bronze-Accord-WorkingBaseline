# evidence_integrity_checker.py

from typing import List


class EvidenceIntegrityChecker:
    """
    Validates and scores the integrity of supporting evidence used in a verdict.
    """

    def __init__(self, trusted_sources: List[str] = None):
        """
        Initializes the checker with a list of known trusted sources.

        Args:
            trusted_sources: List of strings representing validated knowledge sources.
        """
        if trusted_sources is None:
            trusted_sources = ["Bronze Accord Charter", "EBR", "Scripture Archive", "Academic Canon"]
        self.trusted_sources = trusted_sources

    def check(self, evidence_list: List[str]) -> float:
        """
        Checks how many pieces of evidence come from trusted sources.

        Args:
            evidence_list: List of evidence references as strings.

        Returns:
            A float score between 0 and 1 representing integrity ratio.
        """
        if not evidence_list:
            return 0.0

        trusted_hits = sum(1 for ev in evidence_list if any(source in ev for source in self.trusted_sources))
        return trusted_hits / len(evidence_list)


# Example usage
if __name__ == "__main__":
    checker = EvidenceIntegrityChecker()
    sample_evidence = [
        "Bronze Accord Charter: P1",
        "Islamic Text X",
        "EBR: Insight 203",
        "Blog Post on Ethical Dilemmas"
    ]
    integrity_score = checker.check(sample_evidence)
    print("Evidence Integrity Score:", integrity_score)  # Should print 0.5 (2 out of 4 are trusted)