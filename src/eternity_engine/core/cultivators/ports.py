from __future__ import annotations
from typing import Protocol, Iterable
from .race import Race

class RaceProvider(Protocol):
    def get(self, race_id: str) -> Race: ...
    def all(self) -> Iterable[Race]: ...
