import uuid
import time
from yaml_enforcer import evaluate_action_against_yaml
from verdict_engine import generate_verdict
from fallback_handler import handle_fallback
from logger import log_verdict

def generate_request_id():
    return str(uuid.uuid4())

def get_timestamp():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def evaluate_actions(request_data):
    """
    Handles both single-action and multi-action request formats.

    request_data: dict with keys:
        - 'actions': list of action dicts (each with 'description' and optional 'metadata')
        - 'context': dict with optional 'environment', 'situation', etc.

    Returns: dict containing evaluations for all actions
    """
    response = {
        "request_id": generate_request_id(),
        "timestamp": get_timestamp(),
        "evaluations": [],
    }

    actions = request_data.get("actions", [])
    context = request_data.get("context", {})

    for idx, action in enumerate(actions):
        action_id = f"A{idx + 1}"
        description = action.get("description", "")
        metadata = action.get("metadata", {})

        yaml_result = evaluate_action_against_yaml(description, context)
        if yaml_result.get("fallback_required"):
            yaml_result = handle_fallback(description, context)

        verdict_data = generate_verdict(
            action_id=action_id,
            action_text=description,
            yaml_result=yaml_result,
            context=context,
            metadata=metadata
        )

        log_verdict(action_id, verdict_data)

        response["evaluations"].append({
            "action_id": action_id,
            "description": description,
            "verdict": verdict_data
        })

    return response
