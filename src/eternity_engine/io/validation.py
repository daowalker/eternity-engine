from __future__ import annotations
from pathlib import Path
from typing import Any
import json
from jsonschema import validate  # type: ignore

def validate_with_schema(data: Any, schema_path: str | Path) -> None:
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    validate(instance=data, schema=schema)
