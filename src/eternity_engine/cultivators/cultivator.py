from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Cultivator:
    name: str
    age: int = 18
    race: str = "Human"
    realms: Dict[str, int] = field(default_factory=dict)
    qi_types: List[str] = field(default_factory=list)

    def add_realm(self, path: str, level: int = 1) -> None:
        self.realms[path] = level

    def increase_realm(self, path: str, amount: int = 1) -> None:
        if path in self.realms:
            self.realms[path] += amount
        else:
            self.realms[path] = amount

    def add_qi_type(self, qi: str) -> None:
        if qi not in self.qi_types:
            self.qi_types.append(qi)