# manifest_loader.py.md

```python
# ===============================
# Module: manifest_loader.py
# Purpose: Load, parse, and validate the contents of the project ZIP archive manifest
#          and make it accessible to other validation or sync subsystems
# Part of: Manifest Management System
# ===============================

import logging
import json
from framework_models import ManifestData, ManifestLoadResult

logger = logging.getLogger(__name__)

def load_manifest(manifest_path: str) -> ManifestLoadResult:
    """
    Load the structured manifest from a .md file and convert to usable data.

    Args:
        manifest_path (str): Path to the manifest Markdown file.

    Returns:
        ManifestLoadResult: Success flag and parsed ManifestData object or error message.
    """
    logger.info(f"Loading manifest from: {manifest_path}")
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse the JSON segment if present
        start_marker = "```json"
        end_marker = "```"
        if start_marker in content:
            json_start = content.index(start_marker) + len(start_marker)
            json_end = content.index(end_marker, json_start)
            json_block = content[json_start:json_end].strip()
            manifest_data = json.loads(json_block)
            return ManifestLoadResult(success=True, manifest=ManifestData(**manifest_data))
        
        logger.warning("No JSON segment found in manifest.")
        return ManifestLoadResult(success=False, message="Manifest missing JSON block.")

    except Exception as e:
        logger.exception("Failed to load manifest.")
        return ManifestLoadResult(success=False, message=str(e))