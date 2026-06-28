"""Organization simulator helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SimulatorSpec:
    """Machine-readable simulator specification."""

    name: str
    organization_type: str
    departments: tuple[str, ...]
    agents: tuple[str, ...]
    workflows: tuple[str, ...]
    memory_types: tuple[str, ...]
    governance_rules: tuple[str, ...]
    metrics: tuple[str, ...]


def simulator_complexity(spec: SimulatorSpec) -> int:
    """Estimate organization simulator complexity on a 0 to 100 scale."""

    raw = (
        len(spec.departments) * 7
        + len(spec.agents) * 8
        + len(spec.workflows) * 7
        + len(spec.memory_types) * 6
        + len(spec.governance_rules) * 5
        + len(spec.metrics) * 4
    )
    return min(100, raw)


def simulator_readiness_hint(spec: SimulatorSpec) -> str:
    """Return an implementation hint based on simulator complexity."""

    score = simulator_complexity(spec)
    if score >= 85:
        return "start_with_one_pilot_workflow"
    if score >= 65:
        return "sequence_department_pilots"
    return "safe_for_small_scale_rollout"
