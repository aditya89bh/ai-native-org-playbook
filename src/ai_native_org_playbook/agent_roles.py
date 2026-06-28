"""Agent role validation and scoring helpers."""

from __future__ import annotations

from dataclasses import dataclass

REQUIRED_AGENT_ROLE_FIELDS: tuple[str, ...] = (
    "name",
    "purpose",
    "responsibilities",
    "inputs",
    "outputs",
    "permissions",
    "memory_scope",
    "escalation_triggers",
    "evaluation_metrics",
    "failure_modes",
    "department_fit",
)


@dataclass(frozen=True)
class AgentRoleSpec:
    """Machine-readable agent role specification."""

    name: str
    responsibilities: tuple[str, ...]
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    permissions: tuple[str, ...]
    memory_scope: tuple[str, ...]
    escalation_triggers: tuple[str, ...]
    evaluation_metrics: tuple[str, ...]
    department_fit: tuple[str, ...]


def missing_role_fields(field_names: set[str]) -> list[str]:
    """Return required role fields missing from a spec."""

    return [field for field in REQUIRED_AGENT_ROLE_FIELDS if field not in field_names]


def role_operational_depth(spec: AgentRoleSpec) -> int:
    """Estimate role operational depth on a 0 to 100 scale."""

    raw = (
        len(spec.responsibilities) * 7
        + len(spec.inputs) * 4
        + len(spec.outputs) * 4
        + len(spec.permissions) * 5
        + len(spec.memory_scope) * 5
        + len(spec.escalation_triggers) * 5
        + len(spec.evaluation_metrics) * 5
        + len(spec.department_fit) * 3
    )
    return min(100, raw)
