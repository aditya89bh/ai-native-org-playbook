from ai_native_org_playbook.maturity import maturity_level, score_capabilities, weighted_average
from ai_native_org_playbook.models import CapabilityScore, MaturityLevel


def test_weighted_average_scores_capabilities() -> None:
    score = weighted_average([
        CapabilityScore("workflow", 4, 2.0),
        CapabilityScore("governance", 2, 1.0),
    ])
    assert round(score, 2) == 3.33


def test_maturity_level_mapping() -> None:
    assert maturity_level(0.5) == MaturityLevel.AD_HOC
    assert maturity_level(4.5) == MaturityLevel.AI_NATIVE


def test_score_capabilities_default_model() -> None:
    score, level = score_capabilities({
        "workflow_clarity": 4,
        "knowledge_quality": 4,
        "agent_readiness": 3,
        "governance": 3,
        "memory_design": 4,
        "measurement": 3,
        "change_capacity": 4,
    })
    assert round(score, 2) == 3.57
    assert level == MaturityLevel.ORCHESTRATED
