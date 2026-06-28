"""Markdown report helpers for AI-native organization assessments."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReportSection:
    """A named report section."""

    title: str
    lines: tuple[str, ...]


def render_markdown_report(title: str, sections: tuple[ReportSection, ...]) -> str:
    """Render a deterministic markdown report."""

    output: list[str] = [f"# {title}", ""]
    for section in sections:
        output.append(f"## {section.title}")
        output.append("")
        output.extend(section.lines)
        output.append("")
    return "\n".join(output).rstrip() + "\n"


def recommendation_from_score(score: float, low: str, medium: str, high: str) -> str:
    """Return recommendation text from a normalized 0 to 100 score."""

    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score < 40:
        return low
    if score < 70:
        return medium
    return high
