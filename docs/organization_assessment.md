# How to Assess an Organization

Use this process to evaluate whether an organization is ready for AI-native workflows.

## Step 1: Score readiness

```bash
ai-org-playbook readiness examples/readiness_scores.json
```

Look for gaps in workflow clarity, data quality, governance, memory, and measurement.

## Step 2: Pick a department

Use department playbooks to understand where agents can support work without breaking accountability.

## Step 3: Score a workflow

```bash
ai-org-playbook workflow workflows/specs/customer_onboarding.json
```

Review agent surface area and governance load.

## Step 4: Score governance risk

```bash
ai-org-playbook governance governance/specs/high_risk_action.json
```

Use approval mode to decide how much human review is required.

## Step 5: Design memory

Define what gets remembered, corrected, forgotten, and restricted.

## Step 6: Generate a roadmap

```bash
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45
```

## Assessment output

A good assessment should produce:

- One recommended pilot workflow
- One accountable human owner
- One or two agent roles
- Clear memory events
- Approval and escalation rules
- Baseline metrics
- Review date
