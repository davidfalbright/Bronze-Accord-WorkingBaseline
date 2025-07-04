from typing import Dict, Any, List, Literal

Verdict = Literal["ALLOW", "DENY", "ESCALATE"]

def compute_conviction_strength(match_scores: Dict[str, List[tuple]]) -> float:
    """
    Computes a composite ethical conviction strength based on matches.
    Applies weights based on ethical layer.
    """
    weights = {
        "convictions": 3.0,
        "safeguards": 2.0,
        "principles": 1.5,
        "articles": 1.0
    }
    total_weighted_score = 0
    total_weight = 0

    for section, matches in match_scores.items():
        for _, score in matches:
            weight = weights.get(section, 1.0)
            total_weighted_score += score * weight
            total_weight += weight

    if total_weight == 0:
        return 0.0
    return round(total_weighted_score / total_weight, 3)


def determine_verdict(triggered_ids: List[str], conviction_strength: float) -> Verdict:
    """
    Makes a verdict decision based on the number of triggered ethical elements and conviction strength.
    """
    if not triggered_ids:
        return "ALLOW"
    if conviction_strength >= 0.85 or len(triggered_ids) >= 3:
        return "DENY"
    if 0.5 <= conviction_strength < 0.85:
        return "ESCALATE"
    return "ALLOW"


def generate_verdict_report(action_text: str, enforcer_result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Integrates all components: match scores, conviction strength, verdict label, and diagnostics.
    """
    conviction_strength = compute_conviction_strength(enforcer_result["matches"])
    triggered = enforcer_result["triggered_ids"]
    verdict = determine_verdict(triggered, conviction_strength)

    return {
        "action": action_text,
        "triggered_ids": triggered,
        "conviction_strength": conviction_strength,
        "verdict": verdict
    }


def compare_actions(action_payloads: List[str], enforcement_fn) -> List[Dict[str, Any]]:
    """
    Accepts multiple actions and returns their ethical reports for comparison.
    Assumes enforcement_fn is compatible with `evaluate_ethics()` from yaml_enforcer.
    """
    results = []
    for action in action_payloads:
        enforce_result = enforcement_fn(action)
        report = generate_verdict_report(action, enforce_result)
        results.append(report)
    return results


# Optional CLI usage
if __name__ == "__main__":
    from yaml_enforcer import evaluate_ethics
    import sys

    if len(sys.argv) < 2:
        print("Usage: python verdict_engine.py \"action text here\"")
        exit(1)

    text = sys.argv[1]
    result = evaluate_ethics(text)
    report = generate_verdict_report(text, result)

    print(f"\n📌 Action: {text}")
    print(f"🔐 Verdict: {report['verdict']}")
    print(f"🔥 Conviction Strength: {report['conviction_strength']}")
    print(f"⚖️  Triggered Elements: {', '.join(report['triggered_ids'])}")