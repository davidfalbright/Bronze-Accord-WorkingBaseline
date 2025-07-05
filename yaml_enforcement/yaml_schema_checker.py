# ===============================
# Module: yaml_schema_checker.py
# Purpose: Validate that the YAML enforcement block adheres to
#          the expected schema structure and field types
# Part of: YAML Enforcement & Validation
# ===============================

import logging
import yaml
from framework_models import YAMLValidationResult

logger = logging.getLogger(__name__)

REQUIRED_TOP_LEVEL_FIELDS = [
    "convictions", "safeguards", "principles", "articles"
]

def check_yaml_schema(yaml_path: str) -> YAMLValidationResult:
    """
    Load and validate the structural schema of the YAML enforcement file.

    Args:
        yaml_path (str): Path to the YAML file

    Returns:
        YAMLValidationResult: Outcome with success flag and schema issues
    """
    logger.debug(f"Checking YAML schema at: {yaml_path}")

    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        issues = []
        for field in REQUIRED_TOP_LEVEL_FIELDS:
            if field not in data:
                issues.append(f"Missing top-level field: {field}")

        success = len(issues) == 0
        return YAMLValidationResult(success=success, issues=issues)

    except Exception as e:
        logger.exception("YAML schema validation failed.")
        return YAMLValidationResult(success=False, issues=[str(e)])
