from ai_native_org_playbook.cli import build_parser


def _run_command(args: list[str]) -> None:
    parser = build_parser()
    namespace = parser.parse_args(args)
    assert namespace.func(namespace) == 0


def test_readiness_cli_executes(capsys) -> None:  # type: ignore[no-untyped-def]
    _run_command(["readiness", "examples/readiness_scores.json"])
    assert "orchestrated_workflows" in capsys.readouterr().out


def test_workflow_cli_executes(capsys) -> None:  # type: ignore[no-untyped-def]
    _run_command(["workflow", "workflows/specs/customer_onboarding.json"])
    assert "agent_surface_area" in capsys.readouterr().out


def test_roadmap_cli_executes(capsys) -> None:  # type: ignore[no-untyped-def]
    _run_command(["roadmap", "--readiness-score", "3.4", "--governance-risk", "45"])
    assert "AI-Native Transformation Roadmap" in capsys.readouterr().out
