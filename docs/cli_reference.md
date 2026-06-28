# CLI Reference

The CLI exposes the playbook's calculators and report generators.

## Maturity

```bash
ai-org-playbook maturity examples/maturity_scores.json
```

## Readiness

```bash
ai-org-playbook readiness examples/readiness_scores.json
```

## Agent opportunity

```bash
ai-org-playbook opportunity --repetition 5 --context-load 4 --decision-frequency 4 --compliance-risk 1 --human-judgment-required 2 --data-quality 5
```

## Department complexity

```bash
ai-org-playbook department departments/specs/sales.json
```

## Agent role depth

```bash
ai-org-playbook agent-role agent_roles/specs/research_agent.json
```

## Workflow surface area

```bash
ai-org-playbook workflow workflows/specs/customer_onboarding.json
```

## Governance risk

```bash
ai-org-playbook governance governance/specs/high_risk_action.json
```

## Memory policy

```bash
ai-org-playbook memory-policy --tier decision --confidence 0.9
```

## Simulator complexity

```bash
ai-org-playbook simulator simulators/specs/robotics_company.json
```

## Roadmap report

```bash
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```

Write roadmap output to a file:

```bash
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45 --output reports/generated_roadmap.md
```
