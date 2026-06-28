# Agent Role Library

Phase 3 defines reusable agent roles for AI-native organizations.

## Included roles

- Research Agent
- Memory Agent
- Planning Agent
- Compliance Agent
- Analytics Agent
- Customer Support Agent
- Sales Research Agent
- Hiring Agent
- Finance Analyst Agent
- Incident Agent
- Knowledge Agent
- Workflow Orchestration Agent
- Chief of Staff Agent
- Product Feedback Agent
- Design Review Agent

## Design rule

Agents should be roles, not prompts. A usable role needs purpose, inputs, outputs, permissions, memory scope, review triggers, metrics, and failure modes.

## CLI usage

```bash
ai-org-playbook agent-role agent_roles/specs/research_agent.json
```

## Recommended use

Start with a department playbook, choose a pilot workflow, then select one or two agent roles with bounded permissions.
