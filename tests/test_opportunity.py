from ai_native_org_playbook.opportunity import OpportunityFactors, opportunity_band, score_agent_opportunity


def test_agent_opportunity_scoring() -> None:
    score = score_agent_opportunity(OpportunityFactors(5, 4, 4, 1, 2, 5))
    assert score >= 70
    assert opportunity_band(score) in {"human_agent_collaboration", "prime_agent_workflow"}


def test_low_opportunity_band() -> None:
    score = score_agent_opportunity(OpportunityFactors(1, 1, 1, 4, 5, 1))
    assert opportunity_band(score) == "keep_human_led"
