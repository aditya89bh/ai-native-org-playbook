from ai_native_org_playbook.pilot import PilotCandidate, pilot_band, pilot_score


def test_pilot_scoring() -> None:
    score = pilot_score(PilotCandidate(value=5, feasibility=4, risk=2, measurability=5, sponsor_quality=4))
    assert score >= 75
    assert pilot_band(score) == "start_here"
