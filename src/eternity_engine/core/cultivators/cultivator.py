from dataclasses import dataclass
from .race import Race

@dataclass(slots=True)
class Cultivator:
    name: str
    age: int
    race: Race

    def can_absorb_qi(self, qi_type: str) -> bool:
        return self.race.can_absorb_qi(qi_type)