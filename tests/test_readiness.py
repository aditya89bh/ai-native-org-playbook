from ai_native_org_playbook.readiness import readiness_band, readiness_score


def test_readiness_score_and_band() -> None:
    score = readiness_score({
        "workflow_clarity": 4,
        "data_quality": 3,
        "documentation_maturity": 3,
        "governance_maturity": 3,
        "access_control": 4,
        "memory_architecture": 3,
        "review_capacity": 4,
        "measurement_discipline": 3,
        "change_management": 4,
    })
    assert round(score, 2) == 3.44
    assert readiness_band(score) == "orchestrated_workflows"
