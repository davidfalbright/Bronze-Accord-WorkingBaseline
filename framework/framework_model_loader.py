# ===============================
# Module: framework_model_loader.py
# Purpose: Load and deserialize framework model definitions from storage
#          for use by the braid, SAGE, and REST components
# Part of: Framework Models
# ===============================

import json
import logging
from typing import Optional
from framework_models import FrameworkModel, LoadResult

logger = logging.getLogger(__name__)

def load_framework_model(filepath: str) -> LoadResult:
    """
    Load a framework model from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        LoadResult: Loaded model or failure message.
    """
    logger.debug(f"Loading framework model from {filepath}")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        model = FrameworkModel(**data)
        logger.info(f"Framework model loaded: {model.name}")
        return LoadResult(success=True, module=model)
    except Exception as e:
        logger.exception("Failed to load framework model.")
        return LoadResult(success=False, message=str(e), module=None)
