from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Iterable
from jsonschema.exceptions import ValidationError

from eternity_engine.core.cultivators.race import Race
from eternity_engine.core.cultivators.ports import RaceProvider
from eternity_engine.io.config_loader import load_config
from eternity_engine.io.validation import validate_with_schema
from eternity_engine.infra.config_settings import ConfigSettings

@dataclass(slots=True)
class RaceRepository(RaceProvider):
    _by_id: Dict[str, Race]

    @classmethod
    def from_file(cls, config_path, schema_path) -> "RaceRepository":
        config_settings = ConfigSettings()
        data = load_config(config_path)
        validate_with_schema(data, schema_path)
        by_id: Dict[str, Race] = {}
        for item in data:
            r = Race(
                id=item["id"],
                name=item["name"],
                absorb_qi=frozenset(item["absorb_qi"]),
            )
            by_id[r.id] = r
        return cls(by_id)

    def get(self, race_id: str) -> Race:
        try:
            return self._by_id[race_id]
        except KeyError:
            raise KeyError(f"Unknown race id: {race_id!r}")

    def all(self) -> Iterable[Race]:
        return self._by_id.values()
