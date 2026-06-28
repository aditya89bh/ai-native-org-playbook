from ai_native_org_playbook.assessment_reports import build_readiness_report, build_roadmap_report


def test_build_readiness_report() -> None:
    report = build_readiness_report(3.4, "orchestrated_workflows")
    assert "AI-Native Readiness Report" in report
    assert "3.40/5" in report


def test_build_roadmap_report() -> None:
    report = build_roadmap_report(3.4, 45)
    assert "AI-Native Transformation Roadmap" in report
    assert "Recommended actions" in report
