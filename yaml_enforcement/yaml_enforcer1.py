# ===============================
# Module: yaml_enforcer.py
# Purpose: Enforce conformance between the YAML ethical enforcement block
#          and the human-readable Charter text
# Part of: YAML Enforcement Layer
# ===============================

import logging
import yaml
from framework_models import YAMLBlock, EnforcementCheckResult

logger = logging.getLogger(__name__)

def enforce_yaml_block_alignment(yaml_path: str, charter_text: str) -> EnforcementCheckResult:
    """
    Check that the YAML enforcement block is synchronized with the Charter.

    Args:
        yaml_path (str): Path to the YAML file
        charter_text (str): Full Charter in plain text

    Returns:
        EnforcementCheckResult: Summary of matching issues
    """
    logger.debug("Enforcing YAML block alignment...")

    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            block = yaml.safe_load(f)

        block_keys = extract_keys_from_yaml(block)
        missing_keys = [key for key in block_keys if key not in charter_text]

        success = len(missing_keys) == 0
        return EnforcementCheckResult(
            success=success,
            missing_keys=missing_keys,
            total_keys=len(block_keys)
        )

    except Exception as e:
        logger.exception("YAML enforcement check failed.")
        return EnforcementCheckResult(success=False, missing_keys=[], error=str(e))


def extract_keys_from_yaml(yaml_block: dict) -> list:
    """
    Flatten top-level keys from the YAML structure.

    Args:
        yaml_block (dict): Parsed YAML dictionary.

    Returns:
        list: Key paths.
    """
    return list(yaml_block.keys()) if isinstance(yaml_block, dict) else []
