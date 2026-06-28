"""Memory policy helpers."""

from __future__ import annotations

RETENTION_DAYS: dict[str, int | None] = {
    "ephemeral": 30,
    "operational": 180,
    "project": 540,
    "decision": None,
    "policy": None,
    "incident": None,
    "sensitive": 90,
}


def retention_days(tier: str) -> int | None:
    """Return default retention days for a memory tier."""

    normalized = tier.strip().lower()
    if normalized not in RETENTION_DAYS:
        raise ValueError("unknown retention tier")
    return RETENTION_DAYS[normalized]


def should_require_review(tier: str, confidence: float, sensitive: bool) -> bool:
    """Return whether a memory event should require human review."""

    if not 0 <= confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    normalized = tier.strip().lower()
    if normalized not in RETENTION_DAYS:
        raise ValueError("unknown retention tier")
    return sensitive or normalized in {"decision", "policy", "incident"} or confidence < 0.7
