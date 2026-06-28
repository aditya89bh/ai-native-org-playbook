from ai_native_org_playbook.cli import build_parser


def test_cli_has_phase_one_commands() -> None:
    parser = build_parser()
    help_text = parser.format_help()
    assert "maturity" in help_text
    assert "opportunity" in help_text
    assert "memory-map" in help_text
    assert "readiness" in help_text
    assert "pilot" in help_text
    assert "decision-rights" in help_text
