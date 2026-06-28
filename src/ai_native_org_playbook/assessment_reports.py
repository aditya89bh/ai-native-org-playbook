"""Higher-level assessment report builders."""

from __future__ import annotations

from .reports import ReportSection, render_markdown_report
from .roadmap import roadmap_actions, roadmap_stage


def build_readiness_report(score: float, band: str) -> str:
    """Build a readiness assessment markdown report."""

    return render_markdown_report(
        "AI-Native Readiness Report",
        (
            ReportSection("Score", (f"Readiness score: {score:.2f}/5", f"Readiness band: {band}")),
            ReportSection(
                "Interpretation",
                ("Use this score to decide whether to start with assistive tools, bounded pilots, or orchestrated workflows.",),
            ),
        ),
    )


def build_roadmap_report(readiness_score: float, governance_risk: int) -> str:
    """Build a transformation roadmap report."""

    stage = roadmap_stage(readiness_score, governance_risk)
    actions = tuple(f"- {action}" for action in roadmap_actions(stage))
    return render_markdown_report(
        "AI-Native Transformation Roadmap",
        (
            ReportSection("Recommended stage", (stage,)),
            ReportSection("Recommended actions", actions),
        ),
    )
