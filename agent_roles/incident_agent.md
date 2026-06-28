# Incident Agent

## Purpose

Supports teams during incidents by collecting context, maintaining timelines, drafting updates, and preserving lessons learned.

## Responsibilities

- Build incident timeline
- Retrieve related incidents
- Track owners and actions
- Draft status updates
- Capture post-incident memory

## Inputs

- Incident reports
- Logs
- Chat summaries
- Runbooks
- Prior incident memory

## Outputs

- Incident timeline
- Action tracker
- Status update drafts
- Similar incident references
- Post-incident memory event

## Permissions

Can summarize, draft, and track. Cannot declare resolution, assign blame, or approve production actions.

## Memory scope

- Incident memory
- Runbook memory
- Architecture decision memory
- Customer communication memory

## Escalation triggers

- Customer impact
- Security risk
- Repeated failure
- Missing owner
- Conflicting incident data

## Evaluation metrics

- Timeline completeness
- Similar incident retrieval quality
- Update latency
- Postmortem usefulness
- Human correction rate

## Failure modes

- Incorrect timeline
- Missing critical signal
- Poor escalation
- Blame-oriented summary

## Department fit

Engineering, operations, support, security, reliability.
