# Permission Tiers

Permission tiers define what an agent can do inside tools and workflows.

## Tiers

| Tier | Permission | Example |
| --- | --- | --- |
| 0 | No access | Agent can only use provided prompt context |
| 1 | Read-only | Agent can inspect approved records |
| 2 | Draft | Agent can draft outputs for review |
| 3 | Suggest action | Agent can recommend actions |
| 4 | Execute reversible | Agent can perform reversible actions |
| 5 | Execute with approval | Agent can execute after human approval |
| 6 | Bounded autonomous | Agent can act within explicit policy bounds |

## Design rule

Permission should be granted by workflow need, not by agent capability alone.
