# Workflow Orchestration Agent

## Purpose

Coordinates multi-step workflows across humans, agents, tools, memory, and approvals.

## Responsibilities

- Track workflow state
- Route tasks to owners
- Detect blocked steps
- Trigger review paths
- Update workflow memory

## Inputs

- Workflow definition
- Task state
- Owner map
- Approval rules
- Memory events

## Outputs

- Task routing updates
- Blocker alerts
- Review notes
- Workflow state summaries
- Completion reports

## Permissions

Can route, summarize, and update workflow state. Cannot override decision rights or approval rules.

## Memory scope

- Workflow memory
- Decision memory
- Approval memory
- Project memory
- Incident memory

## Review triggers

- Blocked owner
- Missing approval
- Conflicting task state
- Policy boundary
- Repeated workflow failure

## Evaluation metrics

- Handoff latency
- Blocker detection rate
- Review quality
- Workflow completion time
- State accuracy

## Failure modes

- Wrong routing
- Excessive review routing
- Hidden bottleneck
- Incorrect workflow state

## Department fit

Operations, product, engineering, support, finance, HR, executive operations.
