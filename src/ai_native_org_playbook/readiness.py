"""Readiness scoring helpers for AI-native transformation."""

from __future__ import annotations

READINESS_AREAS: tuple[str, ...] = (
    "workflow_clarity",
    "data_quality",
    "documentation_maturity",
    "governance_maturity",
    "access_control",
    "memory_architecture",
    "review_capacity",
    "measurement_discipline",
    "change_management",
)


def readiness_score(scores: dict[str, int]) -> float:
    """Return readiness average on a 0 to 5 scale."""

    missing = sorted(set(READINESS_AREAS) - set(scores))
    if missing:
        raise ValueError(f"missing readiness areas: {', '.join(missing)}")
    values = [scores[area] for area in READINESS_AREAS]
    for value in values:
        if not 0 <= value <= 5:
            raise ValueError("readiness scores must be between 0 and 5")
    return sum(values) / len(values)


def readiness_band(score: float) -> str:
    """Map readiness score to a practical deployment band."""

    if not 0 <= score <= 5:
        raise ValueError("readiness score must be between 0 and 5")
    if score < 2:
        return "assistive_only"
    if score < 3.25:
        return "bounded_pilots"
    if score < 4.25:
        return "orchestrated_workflows"
    return "scale_ai_native_operating_model"
