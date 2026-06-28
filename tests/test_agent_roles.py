from ai_native_org_playbook.agent_roles import AgentRoleSpec, missing_role_fields, role_operational_depth


def test_missing_role_fields_reports_gaps() -> None:
    gaps = missing_role_fields({"name", "purpose", "inputs"})
    assert "responsibilities" in gaps
    assert "inputs" not in gaps


def test_role_operational_depth_scores_spec() -> None:
    spec = AgentRoleSpec(
        name="memory_agent",
        responsibilities=("capture", "retrieve", "correct"),
        inputs=("events", "queries"),
        outputs=("memory records", "retrieval notes"),
        permissions=("read", "draft"),
        memory_scope=("decision", "project"),
        escalation_triggers=("low confidence", "conflict"),
        evaluation_metrics=("relevance", "correction rate"),
        department_fit=("all",),
    )
    assert role_operational_depth(spec) > 50
