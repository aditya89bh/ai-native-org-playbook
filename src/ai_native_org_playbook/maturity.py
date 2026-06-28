"""AI-native organization maturity scoring."""

from __future__ import annotations

from .models import CapabilityScore, MaturityLevel

DEFAULT_CAPABILITIES: tuple[str, ...] = (
    "workflow_clarity",
    "knowledge_quality",
    "agent_readiness",
    "governance",
    "memory_design",
    "measurement",
    "change_capacity",
)


def weighted_average(scores: list[CapabilityScore]) -> float:
    """Return weighted maturity score on a 0 to 5 scale."""

    if not scores:
        raise ValueError("at least one capability score is required")
    total_weight = sum(item.weight for item in scores)
    return sum(item.score * item.weight for item in scores) / total_weight


def maturity_level(score: float) -> MaturityLevel:
    """Map a numeric score to a maturity level."""

    if not 0 <= score <= 5:
        raise ValueError("maturity score must be between 0 and 5")
    if score < 1:
        return MaturityLevel.AD_HOC
    if score < 2:
        return MaturityLevel.ASSISTED
    if score < 3.25:
        return MaturityLevel.AUGMENTED
    if score < 4.25:
        return MaturityLevel.ORCHESTRATED
    return MaturityLevel.AI_NATIVE


def score_capabilities(raw_scores: dict[str, int]) -> tuple[float, MaturityLevel]:
    """Score capabilities using the default unweighted model."""

    missing = sorted(set(DEFAULT_CAPABILITIES) - set(raw_scores))
    if missing:
        raise ValueError(f"missing capability scores: {', '.join(missing)}")
    scores = [CapabilityScore(name=name, score=raw_scores[name]) for name in DEFAULT_CAPABILITIES]
    average = weighted_average(scores)
    return average, maturity_level(average)
