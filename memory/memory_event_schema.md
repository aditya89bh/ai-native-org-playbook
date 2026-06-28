# Memory Event Schema

A memory event is a structured record that captures something the organization may need later.

## Required fields

- Event ID
- Timestamp
- Source
- Actor
- Department
- Workflow
- Memory type
- Summary
- Evidence
- Confidence
- Retention tier
- Access scope
- Correction status

## Optional fields

- Related decision
- Related customer
- Related project
- Related policy
- Tags
- Expiry date
- Review owner

## Design principles

- Store source and confidence together.
- Separate facts from assumptions.
- Make correction possible.
- Make expiry intentional.
- Keep sensitive context scoped.
