import json
import os
from datetime import datetime
from typing import Dict, Any, Optional

LOG_DIRECTORY = "verdict_logs"
LOG_FILENAME = "verdict_audit_log.jsonl"

def ensure_log_directory():
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)

def get_timestamp() -> str:
    return datetime.utcnow().isoformat() + "Z"

def log_verdict(verdict_record: Dict[str, Any], source: Optional[str] = None) -> None:
    """
    Logs a single verdict evaluation result to file, with optional source label (e.g., 'api', 'cli').
    """
    ensure_log_directory()
    entry = {
        "timestamp": get_timestamp(),
        "source": source or "unspecified",
        "verdict": verdict_record
    }

    log_path = os.path.join(LOG_DIRECTORY, LOG_FILENAME)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def list_recent_verdicts(n: int = 10) -> list:
    """
    Loads the last n verdicts from the log file.
    """
    log_path = os.path.join(LOG_DIRECTORY, LOG_FILENAME)
    if not os.path.exists(log_path):
        return []

    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return [json.loads(line) for line in lines[-n:]]


def purge_log():
    """
    Deletes the entire verdict log file.
    """
    log_path = os.path.join(LOG_DIRECTORY, LOG_FILENAME)
    if os.path.exists(log_path):
        os.remove(log_path)


# Optional CLI test
if __name__ == "__main__":
    from verdict_engine import generate_verdict_report
    from yaml_enforcer import evaluate_ethics

    action_text = input("Enter action for logging: ")
    enforcement_result = evaluate_ethics(action_text)
    verdict_report = generate_verdict_report(action_text, enforcement_result)

    log_verdict(verdict_report, source="cli")

    print("✅ Verdict logged.")
    print(json.dumps(verdict_report, indent=2))
