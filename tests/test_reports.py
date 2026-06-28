from ai_native_org_playbook.reports import ReportSection, recommendation_from_score, render_markdown_report


def test_render_markdown_report() -> None:
    report = render_markdown_report(
        "Assessment",
        (ReportSection("Summary", ("Score: 80", "Recommendation: scale")),),
    )
    assert report.startswith("# Assessment")
    assert "## Summary" in report
    assert "Score: 80" in report


def test_recommendation_from_score() -> None:
    assert recommendation_from_score(20, "low", "medium", "high") == "low"
    assert recommendation_from_score(50, "low", "medium", "high") == "medium"
    assert recommendation_from_score(80, "low", "medium", "high") == "high"
