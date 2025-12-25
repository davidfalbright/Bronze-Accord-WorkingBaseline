# Verdict Logger
import json
from datetime import datetime

def log_verdict(verdict, path="logs/verdict_log.jsonl"):
    with open(path, "a") as f:
        f.write(json.dumps({"timestamp": datetime.utcnow().isoformat(), "verdict": verdict}) + "\n")
