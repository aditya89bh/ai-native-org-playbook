from ai_native_org_playbook.roadmap import roadmap_actions, roadmap_stage


def test_roadmap_stage_for_low_readiness() -> None:
    assert roadmap_stage(1.5, 20) == "assistive_tools_only"


def test_roadmap_stage_for_high_risk() -> None:
    assert roadmap_stage(3.8, 90) == "governed_low_risk_pilot"


def test_roadmap_actions() -> None:
    actions = roadmap_actions("bounded_department_pilot")
    assert "select one department" in actions
