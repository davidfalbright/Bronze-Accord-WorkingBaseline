# ===============================
# Module: logger_core.py
# Purpose: Core logger configuration and access point for the
#          Bronze Accord system
# Part of: System Logging Infrastructure
# ===============================

import logging

LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
DEFAULT_LOG_LEVEL = logging.INFO

def initialize_logger(name: str, level: int = DEFAULT_LOG_LEVEL) -> logging.Logger:
    """
    Initialize and configure a named logger.

    Args:
        name (str): Logger name (usually module name)
        level (int): Logging level (default: INFO)

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)
    return logger
