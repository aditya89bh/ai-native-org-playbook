from ai_native_org_playbook.workflows import (
    WorkflowSpec,
    missing_workflow_fields,
    workflow_agent_surface_area,
    workflow_governance_load,
)


def test_missing_workflow_fields_reports_gaps() -> None:
    gaps = missing_workflow_fields({"name", "department", "metrics"})
    assert "human_steps" in gaps
    assert "metrics" not in gaps


def test_workflow_agent_surface_area_scores_shared_steps() -> None:
    spec = WorkflowSpec(
        name="customer onboarding",
        department="support",
        human_steps=("approve plan",),
        agent_steps=("draft plan", "track checklist"),
        shared_steps=("kickoff review",),
        memory_events=("customer goal captured",),
        governance_points=("approve commitments",),
        metrics=("time to value",),
        risks=("misstated commitment",),
    )
    assert workflow_agent_surface_area(spec) == 62
    assert workflow_governance_load(spec) == 17
