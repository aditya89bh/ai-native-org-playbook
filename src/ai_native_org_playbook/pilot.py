"""Pilot selection scoring helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PilotCandidate:
    """Scorecard for an AI-native workflow pilot."""

    value: int
    feasibility: int
    risk: int
    measurability: int
    sponsor_quality: int

    def values(self) -> tuple[int, ...]:
        return (self.value, self.feasibility, self.risk, self.measurability, self.sponsor_quality)


def pilot_score(candidate: PilotCandidate) -> int:
    """Return pilot score from 0 to 100."""

    for value in candidate.values():
        if not 1 <= value <= 5:
            raise ValueError("pilot candidate scores must be between 1 and 5")
    weighted = (
        candidate.value * 0.3
        + candidate.feasibility * 0.25
        + (6 - candidate.risk) * 0.2
        + candidate.measurability * 0.15
        + candidate.sponsor_quality * 0.1
    )
    return round(weighted / 5 * 100)


def pilot_band(score: int) -> str:
    """Map pilot score to a recommendation."""

    if not 0 <= score <= 100:
        raise ValueError("pilot score must be between 0 and 100")
    if score >= 75:
        return "start_here"
    if score >= 55:
        return "promising_after_scoping"
    if score >= 40:
        return "needs_redesign"
    return "avoid_for_now"
