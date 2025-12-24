# framework_model_base.py.md

```python
# ===============================
# Module: framework_model_base.py
# Purpose: Define core shared dataclasses and base types used across
#          the Bronze Accord ethical framework system
# Part of: Framework Models (Shared Core)
# ===============================

from dataclasses import dataclass
from typing import Optional, Any, List

@dataclass
class SystemStatus:
    success: bool
    message: Optional[str] = None

@dataclass
class LoadResult:
    success: bool
    message: Optional[str] = None
    module: Optional[Any] = None

@dataclass
class ActivationStatus:
    success: bool
    message: Optional[str] = None

@dataclass
class ValidationResult:
    success: bool
    message: Optional[str] = None

@dataclass
class ParseResult:
    success: bool
    message: Optional[str] = None
    parsed: Optional[Any] = None

@dataclass
class FallbackResult:
    success: bool
    fallback_used: bool
    message: Optional[str] = None
    verdict: Optional[Any] = None

@dataclass
class AuditReport:
    success: bool
    violations: List[str]

@dataclass
class ManifestLoadResult:
    success: bool
    message: Optional[str] = None
    manifest: Optional[Any] = None

@dataclass
class ValidationReport:
    success: bool
    issues: List[str]

@dataclass
class ConvictionStrengthScore:
    value: float
    detail: Optional[str] = None

@dataclass
class DecisionDifficultyScore:
    value: float
    label: str
