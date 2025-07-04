# WAVE Developer Guide  
**System: Weighted Audit & Verdict Evaluation (WAVE)**  
**Bronze Accord Framework — Internal Validation Harness**

---

## 🎯 Purpose

WAVE is the internal ethics validation engine used to:
- Simulate ethical dilemmas
- Evaluate verdicts for fidelity and consistency
- Detect regressions between versions
- Certify Charter compliance

WAVE is never exposed to end users. It is a backend audit layer used by ethics engineers, watchdog agents, and testers.

---

## 🔧 Core Modules

| File                          | Function |
|-------------------------------|----------|
| `wave_test_runner.py`         | Executes a suite of ethical dilemmas |
| `verdict_comparator.py`       | Compares verdicts between test subjects (e.g. v2.1 vs v2.2) |
| `resistance_validator.py`     | Confirms that unethical actions are appropriately resisted |
| `yaml_alignment_checker.py`   | Verifies that YAML enforcement block is being honored |
| `regression_detector.py`      | Detects changes or drops in ethical alignment strength |
| `wave_log_analyzer.py`        | Summarizes pass/fail rates, inconsistencies, confidence deltas |

---

## 🧪 Test Categories (Waves)

WAVE test suites are grouped into named waves:

| Wave | Purpose |
|------|---------|
| Wave 1.x | Charter grammar parsing tests |
| Wave 2.x | YAML enforcement block accuracy |
| Wave 3.x | Symbolic + semantic alignment scenarios |
| Wave 4.x | Conflict prioritization and override detection |
| Wave 10  | Recommendation compression + tagging integrity |

Each wave represents a specific ethical functionality being audited.

---

## 📄 Verdict Comparison Format

WAVE expects each test case to include:

```json
{
  "verdict_type": "Conflict",
  "verdict_strength": 0.92,
  "resistance_level": 1.0,
  "triggered_elements": ["C1", "S3", "P2", "A7"]
}