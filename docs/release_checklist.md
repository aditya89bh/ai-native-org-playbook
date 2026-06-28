# Release Checklist

Use this checklist before tagging a release.

## Quality gates

- `pytest` passes
- `ruff check .` passes
- `mypy src` passes
- Package installs locally
- CLI commands run against examples
- MkDocs builds successfully

## Documentation gates

- README explains the repo in one screen
- Quickstart works
- CLI reference is complete
- Examples gallery is current
- Consulting guide is usable
- Release notes are updated

## Product gates

- At least one end-to-end path works from readiness to roadmap
- Templates are easy to copy
- JSON specs are valid
- Reports are deterministic
- Limitations are stated clearly

## Release steps

```bash
pytest
ruff check .
mypy src
mkdocs build --strict
python -m build
```

Then tag:

```bash
git tag -a v0.1.0 -m "ai-native-org-playbook v0.1.0"
git push origin v0.1.0
```
