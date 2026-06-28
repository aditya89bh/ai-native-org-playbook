from ai_native_org_playbook.departments import DepartmentSpec, department_complexity, missing_sections


def test_missing_sections_reports_gaps() -> None:
    gaps = missing_sections({"current_operating_model", "metrics"})
    assert "ai_native_redesign" in gaps
    assert "metrics" not in gaps


def test_department_complexity_scores_spec() -> None:
    spec = DepartmentSpec(
        name="sales",
        recommended_agents=("research", "crm", "pipeline"),
        core_workflows=("qualification", "proposal"),
        memory_types=("account", "decision"),
        governance_level="medium",
        metrics=("cycle_time", "win_rate"),
    )
    assert department_complexity(spec) > 40
