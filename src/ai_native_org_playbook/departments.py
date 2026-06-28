"""Department playbook validation helpers."""

from __future__ import annotations

from dataclasses import dataclass

REQUIRED_DEPARTMENT_SECTIONS: tuple[str, ...] = (
    "current_operating_model",
    "ai_native_redesign",
    "human_led_work",
    "agent_assisted_work",
    "agent_executed_work",
    "recommended_agents",
    "core_workflows",
    "memory_map",
    "governance",
    "metrics",
    "risks",
    "maturity_checklist",
)


@dataclass(frozen=True)
class DepartmentSpec:
    """Machine-readable summary of a department playbook."""

    name: str
    recommended_agents: tuple[str, ...]
    core_workflows: tuple[str, ...]
    memory_types: tuple[str, ...]
    governance_level: str
    metrics: tuple[str, ...]


def missing_sections(section_keys: set[str]) -> list[str]:
    """Return required section keys missing from a department spec."""

    return [section for section in REQUIRED_DEPARTMENT_SECTIONS if section not in section_keys]


def department_complexity(spec: DepartmentSpec) -> int:
    """Estimate department redesign complexity on a 0 to 100 scale."""

    raw = (
        len(spec.recommended_agents) * 8
        + len(spec.core_workflows) * 7
        + len(spec.memory_types) * 6
        + len(spec.metrics) * 4
    )
    if spec.governance_level == "high":
        raw += 15
    elif spec.governance_level == "medium":
        raw += 8
    return min(100, raw)
