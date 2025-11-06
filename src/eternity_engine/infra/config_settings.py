from __future__ import annotations
from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class ConfigSettings:
    races_path: str = "configs/races.yaml"
    races_scheme_path: str = "schemas/races.schema.json"
