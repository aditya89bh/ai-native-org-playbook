"""Organizational memory mapping helpers."""

from __future__ import annotations

MEMORY_TYPES: tuple[str, ...] = (
    "decision_memory",
    "meeting_memory",
    "project_memory",
    "customer_memory",
    "policy_memory",
    "incident_memory",
    "learning_memory",
)


def recommend_memory_types(workflow_name: str, risk_level: str, customer_facing: bool) -> list[str]:
    """Recommend memory layers for a workflow."""

    normalized_risk = risk_level.strip().lower()
    if normalized_risk not in {"low", "medium", "high"}:
        raise ValueError("risk_level must be low, medium, or high")

    memories = ["decision_memory", "project_memory", "learning_memory"]
    if "meeting" in workflow_name.lower() or "review" in workflow_name.lower():
        memories.append("meeting_memory")
    if customer_facing:
        memories.append("customer_memory")
    if normalized_risk in {"medium", "high"}:
        memories.extend(["policy_memory", "incident_memory"])
    return sorted(set(memories), key=MEMORY_TYPES.index)
