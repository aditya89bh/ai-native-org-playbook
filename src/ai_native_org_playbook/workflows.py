"""Workflow playbook validation and scoring helpers."""

from __future__ import annotations

from dataclasses import dataclass

REQUIRED_WORKFLOW_FIELDS: tuple[str, ...] = (
    "name",
    "department",
    "human_steps",
    "agent_steps",
    "shared_steps",
    "memory_events",
    "governance_points",
    "metrics",
    "risks",
)


@dataclass(frozen=True)
class WorkflowSpec:
    """Machine-readable workflow specification."""

    name: str
    department: str
    human_steps: tuple[str, ...]
    agent_steps: tuple[str, ...]
    shared_steps: tuple[str, ...]
    memory_events: tuple[str, ...]
    governance_points: tuple[str, ...]
    metrics: tuple[str, ...]
    risks: tuple[str, ...]


def missing_workflow_fields(field_names: set[str]) -> list[str]:
    """Return missing required workflow fields."""

    return [field for field in REQUIRED_WORKFLOW_FIELDS if field not in field_names]


def workflow_agent_surface_area(spec: WorkflowSpec) -> int:
    """Estimate how much of a workflow can be agent-supported on a 0 to 100 scale."""

    total_steps = len(spec.human_steps) + len(spec.agent_steps) + len(spec.shared_steps)
    if total_steps == 0:
        raise ValueError("workflow must include at least one step")
    agent_weight = len(spec.agent_steps) + len(spec.shared_steps) * 0.5
    return round(agent_weight / total_steps * 100)


def workflow_governance_load(spec: WorkflowSpec) -> int:
    """Estimate governance load from governance points and risks."""

    raw = len(spec.governance_points) * 10 + len(spec.risks) * 7
    return min(100, raw)
