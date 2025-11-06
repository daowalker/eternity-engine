from dataclasses import dataclass, field
from typing import FrozenSet

@dataclass(slots=True, frozen=True)
class Race:
    id: str
    name: str
    absorb_qi: FrozenSet[str] = field(default_factory=frozenset)

    def can_absorb_qi(self, qi_type: str) -> bool:
        return qi_type in self.absorb_qi
