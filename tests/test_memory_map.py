from ai_native_org_playbook.memory_map import recommend_memory_types


def test_memory_map_for_customer_workflow() -> None:
    memories = recommend_memory_types("customer onboarding", "medium", True)
    assert "customer_memory" in memories
    assert "policy_memory" in memories
    assert "decision_memory" in memories
