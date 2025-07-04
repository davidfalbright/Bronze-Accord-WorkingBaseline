# ===============================
# Module: manifest_sync.py
# Purpose: Ensure the ZIP archive manifest file reflects the current
#          working directory contents — detect, resolve, and sync differences
# Part of: Manifest Management System
# ===============================

import logging
import os
from framework_models import ManifestData, ManifestSyncReport

logger = logging.getLogger(__name__)

REQUIRED_MANIFEST_FIELDS = ["filename", "path", "status"]

def sync_manifest_with_directory(manifest: ManifestData, directory_path: str) -> ManifestSyncReport:
    """
    Reconcile manifest entries with files present in the project directory.

    Args:
        manifest (ManifestData): Current loaded manifest object.
        directory_path (str): Path to the directory being compared.

    Returns:
        ManifestSyncReport: Summary of discrepancies and sync status.
    """
    logger.info(f"Syncing manifest with directory: {directory_path}")
    actual_files = set(os.listdir(directory_path))
    manifest_files = set(entry.filename for entry in manifest.files)

    missing_in_dir = manifest_files - actual_files
    missing_in_manifest = actual_files - manifest_files

    logger.info(f"Files in manifest but missing in dir: {missing_in_dir}")
    logger.info(f"Files in dir but missing in manifest: {missing_in_manifest}")

    return ManifestSyncReport(
        missing_in_directory=list(missing_in_dir),
        missing_in_manifest=list(missing_in_manifest),
        synced=(not missing_in_dir and not missing_in_manifest)
    )