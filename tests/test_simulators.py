from ai_native_org_playbook.simulators import SimulatorSpec, simulator_complexity, simulator_readiness_hint


def test_simulator_complexity_scores_large_spec() -> None:
    spec = SimulatorSpec(
        name="robotics_company",
        organization_type="robotics",
        departments=("engineering", "product", "operations"),
        agents=("incident", "knowledge", "product_feedback"),
        workflows=("incident_response", "pr_review", "customer_onboarding"),
        memory_types=("incident", "customer", "architecture"),
        governance_rules=("safety approval", "production approval"),
        metrics=("incident time", "review cycle"),
    )
    assert simulator_complexity(spec) > 70
    assert simulator_readiness_hint(spec) in {
        "sequence_department_pilots",
        "start_with_one_pilot_workflow",
    }
