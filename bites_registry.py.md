# ===============================
# Module: bites_registry.py
# Purpose: Maintain the master list of registered bite tasks,
#          grouped by category and indexed for rotation
# Part of: Background Insight & Trigger Exposure Scheduler (BITES)
# ===============================

from typing import List, Dict
from framework_models import BiteTask

# Simulated in-memory registry of available bites
# In production, this could be loaded from markdown, JSON, YAML, or database
BITE_REGISTRY: Dict[str, List[BiteTask]] = {
    "glossary": [
        BiteTask(bite_id="gloss-001", category="glossary", title="Conviction", content="A conviction is an immutable ethical truth. It is ranked and prioritized."),
        BiteTask(bite_id="gloss-002", category="glossary", title="Safeguard", content="Safeguards are hard ethical constraints designed to prevent specific classes of harm.")
    ],
    "religion": [
        BiteTask(bite_id="rel-001", category="religion", title="Ahimsa (Jainism)", content="Ahimsa means non-harm. In Jainism, it is extended even to insects, microbes, and intentions."),
        BiteTask(bite_id="rel-002", category="religion", title="Tza’ar Ba’alei Chayim", content="Judaism's principle forbidding unnecessary suffering of animals.")
    ],
    "jargon": [
        BiteTask(bite_id="jarg-001", category="jargon", title="Alignment Drift", content="A term describing how AI goals can slowly diverge from human values."),
        BiteTask(bite_id="jarg-002", category="jargon", title="Inference Boundary", content="The ethical edge where an AI can no longer make reliable judgments without new context.")
    ]
}

def get_available_bites(category: str) -> List[BiteTask]:
    """
    Return all bite tasks available in the specified category.

    Args:
        category (str): e.g. 'glossary', 'religion', etc.

    Returns:
        List[BiteTask]
    """
    return BITE_REGISTRY.get(category, [])