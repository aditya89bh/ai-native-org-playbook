# Tutorial Path

Follow this path if you are new to the repository.

## Tutorial 1: Understand the concept

Read:

- `frameworks/ai_native_org_definition.md`
- `frameworks/operating_model.md`
- `frameworks/human_agent_responsibility_model.md`

## Tutorial 2: Assess readiness

Run:

```bash
ai-org-playbook readiness examples/readiness_scores.json
```

Then read:

- `frameworks/readiness_assessment.md`
- `templates/readiness_assessment_canvas.md`

## Tutorial 3: Redesign one workflow

Read:

- `workflows/customer_onboarding.md`
- `templates/workflow_spec_canvas.md`

Run:

```bash
ai-org-playbook workflow workflows/specs/customer_onboarding.json
```

## Tutorial 4: Choose agent roles

Read:

- `agent_roles/README.md`
- `agent_roles/customer_support_agent.md`
- `agent_roles/workflow_orchestration_agent.md`

## Tutorial 5: Add memory and governance

Read:

- `memory/memory_event_schema.md`
- `governance/approval_matrix.md`

Run:

```bash
ai-org-playbook memory-policy --tier operational --confidence 0.8
```

## Tutorial 6: Generate a roadmap

Run:

```bash
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```
