# Escalation Patterns

Escalation patterns define when agents stop, ask, route, or hand off work.

## Common triggers

- Low confidence
- Missing context
- Policy conflict
- Sensitive stakeholder
- High financial impact
- Legal exposure
- Security exposure
- Repeated failure

## Patterns

| Pattern | Use |
| --- | --- |
| Ask owner | Missing context or low confidence |
| Route specialist | Domain-specific uncertainty |
| Stop workflow | High-risk unresolved issue |
| Require approval | Consequential action |
| Log for review | Low-risk anomaly |

## Design rule

Escalation must be specific. Broad escalation rules create noise and train people to ignore alerts.
