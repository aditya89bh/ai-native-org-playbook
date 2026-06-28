# Audit Log Model

Audit logs make agent work inspectable.

## Required fields

- Audit ID
- Timestamp
- Agent ID
- Human owner
- Workflow
- Tool used
- Input summary
- Output summary
- Permission tier
- Approval status
- Memory used
- Action taken
- Outcome
- Correction link

## Audit levels

| Level | Use |
| --- | --- |
| Basic | Low-risk summaries and drafts |
| Standard | Workflow actions and customer support |
| Strict | Finance, HR, legal, security, production systems |

## Design rule

Audit should explain what happened and why, not just that an action occurred.
