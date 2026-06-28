# CLI Smoke Commands

Run these after installing the package locally.

```bash
ai-org-playbook maturity examples/maturity_scores.json
ai-org-playbook readiness examples/readiness_scores.json
ai-org-playbook department departments/specs/sales.json
ai-org-playbook agent-role agent_roles/specs/research_agent.json
ai-org-playbook workflow workflows/specs/customer_onboarding.json
ai-org-playbook governance governance/specs/high_risk_action.json
ai-org-playbook memory-policy --tier decision --confidence 0.9
ai-org-playbook simulator simulators/specs/robotics_company.json
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```

Expected result: every command exits successfully and prints JSON or markdown output.
