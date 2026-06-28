# Interactive Tools and Calculators

Phase 7 turns the playbook into executable assessment tools.

## Available CLI tools

- Maturity scoring
- Readiness scoring
- Agent opportunity scoring
- Department complexity scoring
- Workflow surface-area scoring
- Agent role depth scoring
- Governance risk scoring
- Memory policy review
- Simulator complexity scoring
- Roadmap report generation

## Recommended workflow

1. Run readiness assessment.
2. Score a candidate pilot.
3. Score governance risk.
4. Select department, workflow, and agent roles.
5. Generate a roadmap report.

## Example

```bash
ai-org-playbook readiness examples/readiness_scores.json
ai-org-playbook governance governance/specs/high_risk_action.json
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```
