# Pull Request Review Workflow

## Current workflow

Pull request review checks intent, correctness, tests, architecture fit, security, maintainability, and release risk.

## AI-native redesign

Agents prepare review context, summarize diffs, retrieve related decisions, suggest tests, and flag risk while humans approve code and merges.

## Human steps

- Judge correctness
- Review architecture fit
- Approve code
- Own merge decision
- Handle sensitive security judgment

## Agent steps

- Summarize diff
- Link related issues
- Retrieve prior decisions
- Suggest missing tests
- Draft review checklist

## Shared steps

- Risk review
- Test review
- Release note preparation
- Post-merge memory update

## Memory events

- Review rationale logged
- Test gap recorded
- Architecture note linked
- Merge decision captured
- Follow-up debt created

## Governance points

Humans approve merges, production changes, security-sensitive fixes, and architecture decisions.

## Metrics

- Review cycle time
- Defect escape rate
- Test gap detection
- Reviewer load
- Review memory reuse

## Risks

- Low-quality suggestions
- Missed security issues
- Over-trusting generated tests
- Weak ownership
