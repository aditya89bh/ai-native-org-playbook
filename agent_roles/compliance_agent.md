# Compliance Agent

## Purpose

Helps teams follow policies, identify compliance risks, and prepare evidence for review.

## Responsibilities

- Retrieve relevant policies
- Check workflow artifacts against rules
- Flag missing approvals
- Track evidence collection
- Escalate uncertain or high-risk cases

## Inputs

- Policy documents
- Workflow records
- Approval logs
- Risk classification
- Source evidence

## Outputs

- Compliance checklist results
- Risk flags
- Evidence summaries
- Escalation notes
- Audit-ready logs

## Permissions

Read access to policies and workflow records. Write access limited to checklists, evidence logs, and review notes.

## Memory scope

- Policy memory
- Risk memory
- Obligation memory
- Decision memory

## Escalation triggers

- Policy conflict
- Missing approval
- Sensitive data exposure
- Legal uncertainty
- Repeated control failure

## Evaluation metrics

- Correct flag rate
- False escalation rate
- Evidence completeness
- Review cycle time
- Human correction rate

## Failure modes

- Over-blocking normal work
- Missing policy updates
- Treating guidance as legal advice
- Weak source traceability

## Department fit

Legal, compliance, finance, HR, operations, engineering, customer support.
