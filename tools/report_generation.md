# Report Generation

The report helpers produce deterministic markdown output that can be used in consulting notes, internal reviews, or implementation plans.

## Roadmap report

```bash
ai-org-playbook roadmap --readiness-score 3.4 --governance-risk 45 --output reports/generated_roadmap.md
```

## Report design principles

- Keep scores visible.
- Include interpretation.
- Convert scores into action.
- Avoid treating a score as a decision by itself.
- Make human ownership explicit before implementation.
