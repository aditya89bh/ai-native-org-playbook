# Memory Access Scopes

Access scopes define who or what can retrieve a memory.

## Scopes

| Scope | Description |
| --- | --- |
| Public internal | Available across the organization |
| Department | Available within one department |
| Workflow | Available only inside a workflow |
| Project | Available only to a project team |
| Role restricted | Available only to approved roles |
| Sensitive restricted | Requires explicit approval and audit |

## Design rule

The default should not be universal access. Scope memory by actual reuse need.
