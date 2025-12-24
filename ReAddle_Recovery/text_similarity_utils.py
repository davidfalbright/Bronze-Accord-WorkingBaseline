# text_similarity_utils.py

import difflib
import re
from typing import Tuple

class TextSimilarityUtils:
    """
    Provides basic string similarity metrics for use in validation, deduplication, and audit logging.
    """

    @staticmethod
    def normalize(text: str) -> str:
        return re.sub(r'\s+', ' ', text.lower().strip())

    @staticmethod
    def similarity_ratio(a: str, b: str) -> float:
        return difflib.SequenceMatcher(None, TextSimilarityUtils.normalize(a), TextSimilarityUtils.normalize(b)).ratio()

    @staticmethod
    def is_similar(a: str, b: str, threshold: float = 0.9) -> bool:
        return TextSimilarityUtils.similarity_ratio(a, b) >= threshold

    @staticmethod
    def get_diff(a: str, b: str) -> str:
        a_words = TextSimilarityUtils.normalize(a).split()
        b_words = TextSimilarityUtils.normalize(b).split()
        diff = difflib.ndiff(a_words, b_words)
        return '\n'.join(diff)
