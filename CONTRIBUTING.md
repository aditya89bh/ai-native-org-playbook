# Contributing

Thanks for considering a contribution.

This repository is a structured framework and toolkit. Contributions should improve clarity, usability, evidence, or executable tooling.

## Good contributions

- New department playbooks with clear governance and memory design
- New workflow specs with human steps, agent steps, memory events, and risks
- Better CLI calculators or report outputs
- More realistic simulator examples
- Templates that help users run workshops or assessments
- Tests for reusable code

## Contribution standards

- Keep language practical and direct.
- Avoid vague claims about AI transformation.
- Define human accountability before agent autonomy.
- Include governance and memory implications for new workflows.
- Add tests for new Python logic.
- Prefer small focused pull requests.

## Local validation

```bash
python -m pip install -e ".[dev,docs]"
pytest
ruff check .
mypy src
mkdocs build --strict
```

## Documentation style

Use plain language. A founder, operator, consultant, or engineering leader should understand the guidance without needing academic context.
