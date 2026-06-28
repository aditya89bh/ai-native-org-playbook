# Memory Correction Workflow

Memory correction is how the organization updates inaccurate or harmful context.

## Workflow

1. Memory is challenged.
2. Source evidence is reviewed.
3. Human owner confirms correction.
4. Correction event is appended.
5. Future retrieval prefers corrected memory.
6. Old memory remains auditable but marked superseded.

## Correction event fields

- Correction ID
- Original memory ID
- Correction owner
- Reason
- Corrected statement
- Evidence
- Timestamp
- Future retrieval rule

## Design rule

Do not silently overwrite important memory. Append correction events so the organization can audit how its knowledge changed.
