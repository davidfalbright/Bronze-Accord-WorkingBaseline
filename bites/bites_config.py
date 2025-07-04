# ===============================
# Module: bites_config.py
# Purpose: Define configuration options and defaults for the BITES
#          exposure engine, including pacing, categories, and overrides
# Part of: Background Insight & Trigger Exposure Scheduler (BITES)
# ===============================

from dataclasses import dataclass
from typing import List

@dataclass
class BitesConfig:
    """
    BITES configuration structure.
    """
    enable_bites: bool = True
    default_rotation_order: List[str] = (
        "glossary",
        "religion",
        "jargon",
        "charter",
        "history",
        "custom"
    )
    min_days_between_exposures: int = 7
    enable_console_delivery: bool = True
    fallback_to_random_if_empty: bool = True
    log_all_events: bool = True

# Default config instance
BITES_SETTINGS = BitesConfig()
