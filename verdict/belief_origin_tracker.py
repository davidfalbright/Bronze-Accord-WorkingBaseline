# belief_origin_tracker.py

import uuid
from typing import Dict, List

class BeliefOriginTracker:
    """
    Tracks the origin of beliefs used in a decision or verdict,
    including source religion, doctrine, language, and AI interpretation.
    """

    def __init__(self):
        self.tracked_beliefs: Dict[str, Dict] = {}

    def record_belief_origin(
        self,
        belief_id: str,
        source_text: str,
        source_religion: str,
        original_language: str,
        translated_language: str,
        interpretation_summary: str,
        ai_version: str
    ):
        self.tracked_beliefs[belief_id] = {
            "source_text": source_text,
            "source_religion": source_religion,
            "original_language": original_language,
            "translated_language": translated_language,
            "interpretation_summary": interpretation_summary,
            "ai_version": ai_version,
        }

    def get_origin(self, belief_id: str) -> Dict:
        return self.tracked_beliefs.get(belief_id, {})

    def list_all_origins(self) -> List[Dict]:
        return list(self.tracked_beliefs.values())

    def reset(self):
        self.tracked_beliefs.clear()
