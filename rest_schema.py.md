# rest_schema.py.md

```python
# ===============================
# Module: rest_schema.py
# Purpose: Define Pydantic models for input validation and output
#          shaping in REST API endpoints
# Part of: REST Interface Schema
# ===============================

from pydantic import BaseModel, Field
from typing import Optional

class EthicalInput(BaseModel):
    """
    Schema for ethical input submitted via API.
    """
    text: str = Field(..., description="Freeform ethical dilemma text")
    metadata: Optional[dict] = Field(default=None, description="Optional metadata for processing")

class VerdictContext(BaseModel):
    """
    Contextual options for controlling how verdicts are evaluated.
    """
    allow_fallbacks: bool = True
    use_compression: bool = True
    override_mode: Optional[str] = None

class VerdictResponse(BaseModel):
    """
    Final REST response structure returned to clients.
    """
    decision: str
    strength: str
    rationale: str
    success: bool
    source: Optional[str] = None

    @classmethod
    def from_engine_outcome(cls, outcome):
        return cls(
            decision=outcome.verdict.decision,
            strength=outcome.verdict.strength,
            rationale=outcome.verdict.rationale,
            success=True,
            source="braid Engine"
        )