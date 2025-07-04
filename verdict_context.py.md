# ===============================
# Module: verdict_context.py
# Purpose: Define contextual modifiers that influence how a verdict
#          is evaluated, including overrides and toggles
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional

@dataclass
class VerdictContext:
    """
    Contextual flags and modifiers for ethical evaluation.
    """
    allow_fallbacks: bool = True
    use_compression: bool = True
    override_mode: Optional[str] = None