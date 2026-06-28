from ai_native_org_playbook.memory_policy import retention_days, should_require_review


def test_retention_days_returns_defaults() -> None:
    assert retention_days("ephemeral") == 30
    assert retention_days("decision") is None


def test_memory_review_required_for_sensitive_or_low_confidence() -> None:
    assert should_require_review("operational", confidence=0.9, sensitive=True)
    assert should_require_review("operational", confidence=0.5, sensitive=False)
    assert should_require_review("decision", confidence=0.95, sensitive=False)
    assert not should_require_review("operational", confidence=0.95, sensitive=False)
