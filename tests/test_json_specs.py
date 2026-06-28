import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC_DIRS = (
    ROOT / "agent_roles" / "specs",
    ROOT / "departments" / "specs",
    ROOT / "workflows" / "specs",
    ROOT / "memory" / "specs",
    ROOT / "governance" / "specs",
    ROOT / "simulators" / "specs",
)


def test_all_json_specs_are_objects() -> None:
    spec_paths = [path for directory in SPEC_DIRS for path in directory.glob("*.json")]
    assert spec_paths

    for path in spec_paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        assert isinstance(data, dict), path
        assert data, path
