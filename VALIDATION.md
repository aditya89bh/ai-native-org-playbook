# Validation Report

This file records the validation expectations for the v0.1.0 release candidate.

## Automated checks

The CI workflow should run:

```bash
ruff check .
mypy src
pytest
python -m build
```

The docs workflow should run:

```bash
mkdocs build --strict
```

## Added Phase 9 validation coverage

- JSON spec smoke tests
- MkDocs navigation target test
- CLI execution smoke tests
- Package build step in CI
- Documentation index for missing department page
- CLI formatting and JSON typing cleanup

## Manual smoke commands

```bash
ai-org-playbook readiness examples/readiness_scores.json
ai-org-playbook workflow workflows/specs/customer_onboarding.json
ai-org-playbook governance governance/specs/high_risk_action.json
ai-org-playbook simulator simulators/specs/robotics_company.json
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```

## Release condition

Do not tag v0.1.0 until CI and docs checks are green on `main`.
