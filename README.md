# AI Native Organization Playbook

A practical open-source framework for redesigning organizations where humans and AI agents work together.

This repository is not a blog collection. It is a reusable operating model with frameworks, department playbooks, agent role specs, workflow redesigns, memory architecture, governance patterns, simulators, calculators, templates, and reports.

## Core premise

Most companies will not become AI-native by adding chatbots to existing workflows. They become AI-native when their workflows, decision rights, knowledge systems, governance, and metrics are redesigned around agents as first-class operating participants.

## What this repo helps you do

- Assess whether an organization is ready for agentic workflows.
- Redesign departments around human-agent collaboration.
- Define agent roles, permissions, memory, escalation rules, and metrics.
- Build organizational memory systems for decisions, meetings, projects, customers, incidents, and policies.
- Simulate before-and-after operating models.
- Create transformation roadmaps from pilot to scale.

## Quickstart

```bash
git clone https://github.com/aditya89bh/ai-native-org-playbook.git
cd ai-native-org-playbook
python -m pip install -e ".[dev]"
pytest
```

Run a readiness assessment:

```bash
ai-org-playbook readiness examples/readiness_scores.json
```

Score a workflow:

```bash
ai-org-playbook workflow workflows/specs/customer_onboarding.json
```

Generate a roadmap:

```bash
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```

## Repository map

| Area | Purpose |
| --- | --- |
| `frameworks/` | Conceptual models and design methods |
| `departments/` | AI-native redesign guides by function |
| `agent_roles/` | Reusable agent role descriptions and JSON specs |
| `workflows/` | Before/after workflow redesigns and JSON specs |
| `memory/` | Organizational memory schemas, correction, forgetting, retention |
| `governance/` | Risk, approvals, audit, permissions, accountability |
| `metrics/` | KPIs for humans, agents, workflows, and organizations |
| `simulators/` | Example companies and scenario simulations |
| `tools/` | CLI calculator references and report generation docs |
| `templates/` | Canvases, checklists, worksheets, policy templates |
| `reports/` | Sample generated reports |
| `src/ai_native_org_playbook/` | CLI, calculators, generators, and validation helpers |
| `tests/` | Test coverage for reusable tooling |

## Current layers

1. Frameworks
2. Department playbooks
3. Agent role library
4. Workflow library
5. Memory and governance controls
6. Simulators and examples
7. Interactive tools and calculators
8. Documentation site and product polish

## Who this is for

- Founders redesigning operations around agents
- Consultants building AI transformation assessments
- Product and ops leaders selecting agent pilots
- Engineering teams designing internal agent workflows
- Researchers studying human-agent organizations

## Design rule

Do not start with automation. Start with work: workflows, decisions, memory, governance, and measurable outcomes.

## Status

Active build toward a polished v0.1.0 release.
