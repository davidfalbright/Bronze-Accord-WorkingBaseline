# manifest_validator.py.md

```python
# ===============================
# Module: manifest_validator.py
# Purpose: Validate the loaded manifest against project rules, ensuring
#          correct filenames, no duplicates, required entries, and compliance
# Part of: Manifest Enforcement and Validation System
# ===============================

import logging
from framework_models import ManifestData, ValidationReport

logger = logging.getLogger(__name__)

REQUIRED_FILES = [
    "README.md",
    "manifest.txt",
    "Charter_v2.2.md",
    "Workspace_Functionality_Restore_Guide.md"
]

def validate_manifest(manifest: ManifestData) -> ValidationReport:
    """
    Validate the structure and contents of a loaded manifest.

    Args:
        manifest (ManifestData): Parsed manifest from loader.

    Returns:
        ValidationReport: Outcome report of validity and issues.
    """
    logger.info("Validating manifest contents...")
    issues = []

    filenames = [entry.filename for entry in manifest.files]

    # Check for required files
    for required in REQUIRED_FILES:
        if required not in filenames:
            issues.append(f"Missing required file: {required}")

    # Check for duplicates
    if len(filenames) != len(set(filenames)):
        issues.append("Duplicate filenames found in manifest.")

    # Enforce naming conventions
    for filename in filenames:
        if " " in filename:
            issues.append(f"Invalid filename (contains space): {filename}")
        if filename.endswith(".md") is False:
            issues.append(f"Non-markdown file included: {filename}")

    logger.info("Manifest validation complete.")
    return ValidationReport(success=(len(issues) == 0), issues=issues)