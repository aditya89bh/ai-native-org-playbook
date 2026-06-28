# v0.1.0 Release Candidate

This repository is ready for final manual validation before tagging `v0.1.0`.

## Final validation commands

```bash
python -m pip install -e ".[dev,docs]"
ruff check .
mypy src
pytest
mkdocs build --strict
python -m build
```

## CLI smoke commands

```bash
ai-org-playbook readiness examples/readiness_scores.json
ai-org-playbook workflow workflows/specs/customer_onboarding.json
ai-org-playbook governance governance/specs/high_risk_action.json
ai-org-playbook simulator simulators/specs/robotics_company.json
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```

## Tagging commands

Run only after CI and docs checks are green on `main`.

```bash
git pull origin main
git tag -a v0.1.0 -m "ai-native-org-playbook v0.1.0"
git push origin v0.1.0
```

## GitHub release title

```text
ai-native-org-playbook v0.1.0
```

## GitHub release summary

```text
Initial release candidate for a practical AI-native organization design toolkit with frameworks, department playbooks, agent roles, workflows, memory/governance controls, simulators, CLI calculators, and documentation.
```

## Release condition

Do not publish the GitHub release until validation is green.
