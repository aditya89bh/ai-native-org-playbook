"""Decision rights recommendation helpers."""

from __future__ import annotations


def recommend_decision_level(risk: int, reversibility: int, ambiguity: int, confidence: int) -> str:
    """Recommend an agent decision-right level.

    Inputs use 1 to 5 scales. Higher reversibility and confidence increase autonomy.
    Higher risk and ambiguity reduce autonomy.
    """

    values = (risk, reversibility, ambiguity, confidence)
    for value in values:
        if not 1 <= value <= 5:
            raise ValueError("decision factors must be between 1 and 5")

    autonomy_score = reversibility + confidence - risk - ambiguity
    if autonomy_score <= -4:
        return "inform_only"
    if autonomy_score <= -2:
        return "draft_only"
    if autonomy_score <= 0:
        return "recommend_options"
    if autonomy_score <= 2:
        return "execute_after_approval"
    return "bounded_autonomous_execution"
