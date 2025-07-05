# rest_status_codes.py.md

```python
# ===============================
# Module: rest_status_codes.py
# Purpose: Centralized definition of HTTP status codes and
#          error messaging used across REST interface
# Part of: REST Interface Utility Layer
# ===============================

HTTP_STATUS = {
    "SUCCESS": 200,
    "BAD_REQUEST": 400,
    "UNAUTHORIZED": 401,
    "FORBIDDEN": 403,
    "NOT_FOUND": 404,
    "SERVER_ERROR": 500
}

ERROR_MESSAGES = {
    "parse_failure": "Unable to parse ethical input.",
    "validation_failure": "Input failed braid structural validation.",
    "engine_failure": "Verdict engine returned no result.",
    "fallback_unavailable": "No fallback logic matched input case.",
    "internal_error": "Internal system error encountered."
}
