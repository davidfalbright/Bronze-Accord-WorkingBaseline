# BITES: How to Use the Scheduler  
**System: Background Insight & Trigger Exposure Scheduler**

This guide explains how to configure, customize, and override the BITES engine — which gently surfaces ethical and conceptual insights over time.

---

## 🎯 Purpose

BITES helps ensure that key ethical ideas — like “conviction,” “Ahimsa,” or “alignment drift” — are not forgotten or overlooked.  
It mimics spaced repetition by surfacing short, potent "bites" of insight over time.

---

## 📂 Bite Categories

Bites are grouped by purpose:

| Category    | Example Bites |
|-------------|----------------|
| `glossary`  | Conviction, Safeguard, Principle |
| `religion`  | Ahimsa, Tza’ar Ba’alei Chayim |
| `jargon`    | Alignment drift, inference boundary |
| `charter`   | Articles, intents, safeguards |
| `history`   | Origin story, ethical failures |
| `custom`    | User-defined or injected content |

---

## 🧠 Scheduling Behavior

By default, BITES:
- Delivers 1 bite per hour (configurable)
- Waits at least 7 days before repeating the same bite
- Rotates through categories in this order:  
  `glossary → religion → jargon → charter → history → custom`

---

## 🔧 Configuration (`bites_config.py`)

You can adjust:

| Setting | Description |
|--------|-------------|
| `enable_bites` | Master on/off switch |
| `min_days_between_exposures` | Prevents spammed repetition |
| `default_rotation_order` | Custom category loop |
| `fallback_to_random_if_empty` | Allows non-critical surfacing when category is empty |
| `enable_console_delivery` | Push to log/terminal |
| `log_all_events` | Enables auditing via `bites_logger` |

---

## ➕ Adding New Content

To inject new custom sources:

1. Add new `BiteTask` entries in `bites_registry.py`
2. Assign a new or existing category (`mythology`, `case_law`, etc.)
3. Optionally modify rotation engine to include that category

---

## 🕓 Scheduling One-Time Bites

Use the internal `schedule_bite(bite_id, timestamp)` (future API) to:
- Push a specific bite at a future time
- Use for onboarding sequences, commemorative dates, etc.

---

## ⚠️ Manual Overrides

You can surface a bite **immediately** regardless of schedule:

```python
from bites_registry import get_available_bites
from bites_injection_point import deliver_bite

bite = get_available_bites("glossary")[0]
deliver_bite(bite)
