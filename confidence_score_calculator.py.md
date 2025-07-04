# confidence_score_calculator.py

from typing import List, Dict
import math


class ConfidenceScoreCalculator:
    """
    Calculates a confidence score for the final ethical verdict based on
    rule alignment coverage, semantic distance, and ethical consistency.
    """

    def __init__(self):
        self.max_possible_score = 1.0

    def calculate(
        self,
        matched_elements: List[str],
        total_possible_elements: int,
        semantic_similarity: float,
        structural_consistency: float
    ) -> float:
        """
        Calculates an aggregate confidence score.

        Args:
            matched_elements (List[str]): Ethical elements triggered by the analysis.
            total_possible_elements (int): Count of elements that could have been triggered.
            semantic_similarity (float): Value between 0 and 1.
            structural_consistency (float): Value between 0 and 1.

        Returns:
            float: Confidence score between 0.0 and 1.0
        """
        if total_possible_elements == 0:
            return 0.0

        coverage_ratio = len(set(matched_elements)) / total_possible_elements
        score = (
            0.4 * coverage_ratio +
            0.3 * semantic_similarity +
            0.3 * structural_consistency
        )
        return round(min(score, self.max_possible_score), 4)