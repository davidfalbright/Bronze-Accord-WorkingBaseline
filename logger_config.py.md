# ===============================
# Module: logger_config.py
# Purpose: Define centralized logging configuration settings
#          used across the Bronze Accord system
# Part of: System Logging Infrastructure
# ===============================

import logging
from typing import Dict

LOGGING_LEVELS: Dict[str, int] = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

DEFAULT_LOG_LEVEL = "INFO"

def get_log_level(level_name: str) -> int:
    """
    Convert string name to logging module level constant.

    Args:
        level_name (str): One of DEBUG, INFO, WARNING, ERROR, CRITICAL

    Returns:
        int: Corresponding logging level (default to INFO if unknown)
    """
    level = LOGGING_LEVELS.get(level_name.upper(), logging.INFO)
    return level