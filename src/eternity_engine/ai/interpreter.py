from __future__ import annotations
from typing import Mapping
from .ports import AIBackend, AIInterpreter


_SYSTEM_PROMPT = (
    "You are the narrator of a Xianxia cultivation simulation game. "
    "Your tone is calm, immersive, and cinematic — never poetic or exaggerated. "
    "Describe events as they unfold, focusing on atmosphere, emotion, and outcome. "
    "Do not use flowery metaphors or archaic words."
)


class NarrationInterpreter(AIInterpreter):

    def __init__(self, backend: AIBackend):
        self.backend = backend

    def narrate_event(
        self,
        *,
        world: Mapping,
        actor: Mapping,
        event: Mapping,
    ) -> str:
        context = (
            f"World Qi Density: {world.get('qi_density', 'Unknown')}\n"
            f"Qi Types: {', '.join(world.get('qi_types', []))}\n"
            f"Region: {world.get('region_name', 'Unnamed Region')}\n\n"
            f"Cultivator: {actor.get('name', 'Unknown')}\n"
            f"Realm: {actor.get('realm', 'Unknown')}\n"
            f"Qi Summary: {actor.get('qi_summary', '-')}\n"
            f"Affiliation: {actor.get('affiliation', '-')}\n\n"
            f"Event: {event.get('title', 'Untitled')}\n"
            f"Description: {event.get('description', '')}"
        )

        prompt = (
            "Describe what happens next in 3–5 sentences. "
            "Keep the tone cinematic but realistic. "
            "Include physical sensations, environment, and the cultivator’s focus, "
            "but avoid excessive detail or ornamentation."
        )

        return self.backend.generate(
            prompt,
            system=_SYSTEM_PROMPT,
            context=context,
            temperature=0.65,
        )
