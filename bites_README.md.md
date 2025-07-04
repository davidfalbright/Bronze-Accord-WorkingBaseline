# BITES — Background Insight & Trigger Exposure Scheduler

**BITES** is a foundational module of the Bronze Accord system. It ensures that critical ethical knowledge — including glossaries, religious insights, technical jargon, and historical precedents — are **periodically surfaced** in a controlled, rotating, and non-intrusive way.

This supports:
- Gentle reinforcement of ethical principles
- Gradual AI self-awareness building
- Long-term human training and ethical recall

---

## 🔧 Key Functions

| File                        | Purpose                                                      |
|-----------------------------|--------------------------------------------------------------|
| `bites_scheduler.py`        | Main timed loop for running bite exposures                   |
| `bites_rotation_engine.py`  | Controls category order and bite selection logic             |
| `bites_tracker.py`          | Tracks which bites have been shown recently                  |
| `bites_injection_point.py`  | Surfaces the bite into logs, memory, UI, or console          |
| `bites_registry.py`         | Master list of available bite definitions                    |
| `bites_logger.py`           | Audits exposure events, failures, and skips                  |
| `bites_config.py`           | Configuration for pacing, categories, and fallback behavior  |

---

## 🎯 Target Categories

BITES rotates among bite types like:

- Glossary definitions (`conviction`, `safeguard`, etc.)
- Religious ethics (e.g. *Ahimsa*, *Tza’ar Ba’alei Chayim*)
- Domain-specific jargon (e.g. `alignment drift`, `belief stack`)
- Charter clauses and ethical history

Each bite is delivered **only if it hasn’t been recently shown**, and each one is logged to preserve spacing.

---

## 📦 Integration Points

- **braid**: Optional memory-surface tagging
- **Logger**: Verbose output in dedicated `bites_logger`
- **REST API (future)**: Low-priority exposure in API responses or tooltips
- **Training**: Part of long-term ethical reinforcement in onboarding scripts

---

## 🔒 Safeguards

- No repeat exposure within 7-day minimum (configurable)
- Skips disabled bites
- Graceful failover if no bite is available (can fallback to random)

---

BITES helps the Accord remember what matters — even when no one is watching.