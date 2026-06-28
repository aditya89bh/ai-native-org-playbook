from ai_native_org_playbook.decision_rights import recommend_decision_level


def test_decision_rights_reduce_autonomy_for_risk() -> None:
    assert recommend_decision_level(risk=5, reversibility=1, ambiguity=5, confidence=2) == "inform_only"


def test_decision_rights_allow_bounded_autonomy() -> None:
    assert recommend_decision_level(risk=1, reversibility=5, ambiguity=1, confidence=5) == "bounded_autonomous_execution"
