from __future__ import annotations
from typing import Protocol, Mapping, Optional

class AIBackend(Protocol):
    def generate(
        self,
        prompt: str,
        *,
        system: str = "",
        context: Optional[str] = None,
        temperature: float = 0.7,
    ) -> str: ...

class AIInterpreter(Protocol):
    def narrate_event(
        self,
        *,
        world: Mapping,
        actor: Mapping,
        event: Mapping,
    ) -> str: ...