# Workflow Library

Phase 4 defines reusable AI-native workflow playbooks.

## Included workflows

- Hiring pipeline
- Sales pipeline
- Customer onboarding
- Sprint planning
- Pull request review
- Product discovery
- Incident response
- Budget planning
- Meeting management
- Knowledge management
- Campaign planning
- Vendor onboarding

## CLI usage

```bash
ai-org-playbook workflow workflows/specs/customer_onboarding.json
```

The command returns:

- Agent surface area
- Governance load

## Design rule

Do not automate isolated tasks first. Redesign the workflow, then assign human steps, agent steps, shared steps, memory events, and governance points.
