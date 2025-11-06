from __future__ import annotations
from pathlib import Path
from typing import Any
import json

def load_config(path: str | Path) -> Any:
    p = Path(path)
    if p.suffix.lower() == ".json":
        return json.loads(p.read_text(encoding="utf-8"))
    if p.suffix.lower() in {".yaml", ".yml"}:
        import ruamel.yaml  # type: ignore
        yaml = ruamel.yaml.YAML(typ="safe")
        return yaml.load(p.read_text(encoding="utf-8"))
    raise ValueError(f"Unsupported format: {p.suffix}")
