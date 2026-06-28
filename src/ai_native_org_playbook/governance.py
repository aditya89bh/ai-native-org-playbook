"""Governance scoring helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GovernanceRisk:
    """Risk factors for agent governance."""

    financial_impact: int
    customer_impact: int
    employee_impact: int
    legal_exposure: int
    reversibility: int
    public_visibility: int

    def values(self) -> tuple[int, ...]:
        return (
            self.financial_impact,
            self.customer_impact,
            self.employee_impact,
            self.legal_exposure,
            self.reversibility,
            self.public_visibility,
        )


def governance_risk_score(risk: GovernanceRisk) -> int:
    """Return governance risk score from 0 to 100."""

    for value in risk.values():
        if not 0 <= value <= 5:
            raise ValueError("governance risk values must be between 0 and 5")
    raw = (
        risk.financial_impact * 0.2
        + risk.customer_impact * 0.2
        + risk.employee_impact * 0.2
        + risk.legal_exposure * 0.2
        + (5 - risk.reversibility) * 0.1
        + risk.public_visibility * 0.1
    )
    return round(raw / 5 * 100)


def approval_mode(score: int) -> str:
    """Map governance risk score to approval mode."""

    if not 0 <= score <= 100:
        raise ValueError("governance score must be between 0 and 100")
    if score >= 80:
        return "dual_approval"
    if score >= 60:
        return "pre_approval"
    if score >= 40:
        return "sampled_review"
    if score >= 20:
        return "batch_review"
    return "no_approval"
