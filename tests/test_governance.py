from ai_native_org_playbook.governance import GovernanceRisk, approval_mode, governance_risk_score


def test_governance_risk_score_maps_to_approval() -> None:
    score = governance_risk_score(
        GovernanceRisk(
            financial_impact=5,
            customer_impact=4,
            employee_impact=4,
            legal_exposure=5,
            reversibility=1,
            public_visibility=4,
        )
    )
    assert score >= 80
    assert approval_mode(score) == "dual_approval"


def test_low_governance_risk_allows_light_approval() -> None:
    score = governance_risk_score(
        GovernanceRisk(
            financial_impact=0,
            customer_impact=1,
            employee_impact=0,
            legal_exposure=0,
            reversibility=5,
            public_visibility=0,
        )
    )
    assert approval_mode(score) == "no_approval"
