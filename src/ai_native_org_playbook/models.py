"""Core typed models used by the playbook tools."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class MaturityLevel(str, Enum):
    """Five-level maturity model for AI-native organizations."""

    AD_HOC = "ad_hoc"
    ASSISTED = "assisted"
    AUGMENTED = "augmented"
    ORCHESTRATED = "orchestrated"
    AI_NATIVE = "ai_native"


@dataclass(frozen=True)
class CapabilityScore:
    """Score for one organization capability."""

    name: str
    score: int
    weight: float = 1.0

    def __post_init__(self) -> None:
        if not 0 <= self.score <= 5:
            raise ValueError("capability score must be between 0 and 5")
        if self.weight <= 0:
            raise ValueError("capability weight must be positive")


@dataclass(frozen=True)
class AgentRole:
    """Specification for an organizational agent role."""

    name: str
    purpose: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    permissions: tuple[str, ...]
    escalation_triggers: tuple[str, ...]
    memory_scope: tuple[str, ...]


@dataclass(frozen=True)
class WorkflowStep:
    """Single step in a workflow redesign."""

    name: str
    owner: str
    agent_supported: bool
    decision_right: str
    memory_event: str | None = None
