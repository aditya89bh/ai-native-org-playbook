"""Agent opportunity scoring for organizational workflows."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OpportunityFactors:
    """Factors for deciding whether a workflow is a good agent candidate."""

    repetition: int
    context_load: int
    decision_frequency: int
    compliance_risk: int
    human_judgment_required: int
    data_quality: int

    def values(self) -> tuple[int, ...]:
        return (
            self.repetition,
            self.context_load,
            self.decision_frequency,
            self.compliance_risk,
            self.human_judgment_required,
            self.data_quality,
        )


def score_agent_opportunity(factors: OpportunityFactors) -> int:
    """Return 0 to 100 agent opportunity score."""

    for value in factors.values():
        if not 0 <= value <= 5:
            raise ValueError("all opportunity factors must be between 0 and 5")

    positive = (
        factors.repetition * 0.25
        + factors.context_load * 0.2
        + factors.decision_frequency * 0.2
        + factors.data_quality * 0.2
    )
    negative = factors.compliance_risk * 0.075 + factors.human_judgment_required * 0.075
    normalized = max(0.0, min(5.0, positive - negative))
    return round(normalized / 5 * 100)


def opportunity_band(score: int) -> str:
    """Convert opportunity score to a recommendation band."""

    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 75:
        return "prime_agent_workflow"
    if score >= 50:
        return "human_agent_collaboration"
    if score >= 30:
        return "assistive_ai_only"
    return "keep_human_led"
