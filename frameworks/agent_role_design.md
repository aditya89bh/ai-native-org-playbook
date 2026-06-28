# Agent Role Design

Agents should be designed as roles, not prompts.

## Role components

1. Purpose
2. Workflow ownership
3. Inputs
4. Outputs
5. Tools
6. Permissions
7. Memory scope
8. Escalation triggers
9. Evaluation metrics
10. Retirement criteria

## Bad role design

"Use AI to help sales."

## Better role design

"Sales Research Agent enriches account context, retrieves prior relationship memory, drafts account briefs, and escalates uncertain claims to the account owner."

## Design rule

If a role cannot be evaluated, it is not specific enough.
