# ===============================
# Module: load_result.py
# Purpose: Represent the outcome of loading a module, resource,
#          or data structure at runtime
# Part of: Framework Models
# ===============================

from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class LoadResult:
    """
    Result of a load operation (e.g., config, model, module).
    """
    success: bool
    message: Optional[str] = None
    module: Optional[Any] = None