from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache

from eternity_engine.infra.config_settings import ConfigSettings
from eternity_engine.infra.config.race_repo import RaceRepository
from eternity_engine.core.cultivators.ports import RaceProvider

@dataclass(slots=True, frozen=True)
class WorldCatalog:
    races: RaceProvider

def build_catalog(settings: ConfigSettings) -> WorldCatalog:
    races = RaceRepository.from_file(settings.races_path)
    return WorldCatalog(races=races)

@lru_cache(maxsize=1)
def get_catalog(settings: ConfigSettings | None = None) -> WorldCatalog:
    return build_catalog(settings or ConfigSettings())

def reload_catalog(settings: ConfigSettings | None = None) -> None:
    get_catalog.cache_clear()
    get_catalog(settings)
