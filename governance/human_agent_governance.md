# Human-Agent Governance

Governance defines what agents can do, when humans approve, and how mistakes are detected.

## Permission levels

1. Read-only
2. Draft-only
3. Suggest action
4. Execute reversible action
5. Execute high-impact action with approval
6. Autonomous execution within bounded policy

## Escalation triggers

- Confidence below threshold
- Policy conflict
- Novel situation
- Customer or employee harm risk
- Legal, financial, or reputational exposure

## Audit requirements

Every agent action should record:

- Actor
- Tool used
- Input context
- Output
- Decision basis
- Human approval state
- Result
