# verdict_logger.py

import json
from datetime import datetime
from pathlib import Path
from framework_models import EvaluatedVerdict

class VerdictLogger:
    def __init__(self, log_dir="verdict_logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def log_verdict(self, verdict: EvaluatedVerdict):
        timestamp = datetime.utcnow().isoformat()
        entry = {
            "timestamp": timestamp,
            "conflict": {
                "source_1": verdict.conflict.source_1,
                "source_2": verdict.conflict.source_2,
                "triggered_elements": verdict.conflict.triggered_elements,
                "description": verdict.conflict.description
            },
            "strength_score": verdict.strength_score,
            "severity_level": verdict.severity_level,
            "supporting_evidence": verdict.supporting_evidence
        }

        filename = f"{timestamp.replace(':', '_')}_verdict.json"
        filepath = self.log_dir / filename
        with open(filepath, "w") as f:
            json.dump(entry, f, indent=2)

    def list_logs(self):
        return sorted(self.log_dir.glob("*.json"))

    def read_log(self, filename):
        path = self.log_dir / filename
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return None
