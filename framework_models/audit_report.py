# ===============================
# Module: audit_report.py
# Purpose: Represent the result of a compliance or archive audit
#          performed on project files or manifests
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import List

@dataclass
class AuditReport:
    """
    Result of running a system or ZIP compliance audit.
    """
    success: bool
    violations: List[str]
