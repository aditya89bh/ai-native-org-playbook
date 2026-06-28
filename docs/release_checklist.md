# Release Checklist

Use this checklist before tagging a release.

## Quality gates

- `pytest` passes
- `ruff check .` passes
- `mypy src` passes
- `python -m build` passes
- `mkdocs build --strict` passes
- CLI commands run against examples
- JSON spec smoke tests pass
- MkDocs navigation target test passes

## Documentation gates

- README explains the repo in one screen
- Quickstart works
- CLI reference is complete
- Examples gallery is current
- Consulting guide is usable
- Organization assessment guide is usable
- Release notes are updated
- Limitations are stated clearly

## Product gates

- At least one end-to-end path works from readiness to roadmap
- Templates are easy to copy
- JSON specs are valid
- Reports are deterministic
- Department, workflow, role, simulator, memory, and governance layers connect clearly

## Release steps

```bash
pytest
ruff check .
mypy src
mkdocs build --strict
python -m build
```

Then tag only after checks are green:

```bash
git tag -a v0.1.0 -m "ai-native-org-playbook v0.1.0"
git push origin v0.1.0
```
