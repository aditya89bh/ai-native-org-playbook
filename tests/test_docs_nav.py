import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_mkdocs_nav_targets_exist() -> None:
    mkdocs = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    docs_paths = sorted(set(re.findall(r"docs/[A-Za-z0-9_./-]+\.md", mkdocs)))
    assert docs_paths

    for docs_path in docs_paths:
        assert (ROOT / docs_path).exists(), docs_path
