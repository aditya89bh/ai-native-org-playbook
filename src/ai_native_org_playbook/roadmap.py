"""Transformation roadmap generation helpers."""

from __future__ import annotations


def roadmap_stage(readiness_score: float, governance_risk: int) -> str:
    """Recommend transformation stage from readiness and governance risk."""

    if not 0 <= readiness_score <= 5:
        raise ValueError("readiness_score must be between 0 and 5")
    if not 0 <= governance_risk <= 100:
        raise ValueError("governance_risk must be between 0 and 100")

    if readiness_score < 2:
        return "assistive_tools_only"
    if governance_risk >= 75:
        return "governed_low_risk_pilot"
    if readiness_score < 3.25:
        return "bounded_department_pilot"
    if readiness_score < 4.25:
        return "orchestrated_workflow_rollout"
    return "scale_ai_native_operating_model"


def roadmap_actions(stage: str) -> tuple[str, ...]:
    """Return recommended actions for a roadmap stage."""

    actions = {
        "assistive_tools_only": (
            "document core workflows",
            "improve data and knowledge quality",
            "start with drafting and summarization agents",
        ),
        "governed_low_risk_pilot": (
            "choose a low-risk pilot workflow",
            "define approval thresholds",
            "add audit logs and human owner",
        ),
        "bounded_department_pilot": (
            "select one department",
            "define agent roles and memory scope",
            "measure before and after workflow metrics",
        ),
        "orchestrated_workflow_rollout": (
            "connect agents across workflows",
            "standardize governance patterns",
            "expand memory correction and retention rules",
        ),
        "scale_ai_native_operating_model": (
            "standardize role families",
            "scale simulator-backed planning",
            "review organization-level operating metrics",
        ),
    }
    if stage not in actions:
        raise ValueError("unknown roadmap stage")
    return actions[stage]
