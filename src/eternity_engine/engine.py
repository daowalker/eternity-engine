from eternity_engine.ai.backend_ollama import OllamaBackend
from eternity_engine.ai.interpreter import NarrationInterpreter

class EternityEngine:
    def __init__(self):
        self.backend = OllamaBackend(model="qwen3:8b")
        self.narrator = NarrationInterpreter(self.backend)
        self.world = None
        self.event_manager = None

    def tick(self):
        world = {
            "qi_density": "High",
            "qi_types": ["Dragon Qi", "Yin Qi"],
            "region_name": "Azure Moon Valley",
        }
        actor = {
            "name": "Liang Feng",
            "realm": "Core Formation (Early)",
            "qi_summary": "Dragon Qi 120, Yin Qi 40",
            "affiliation": "Azure Moon Sect",
        }
        event = {
            "title": "Breakthrough Attempt",
            "description": (
                "Liang Feng focuses under the moonlight, trying to stabilize his Qi flow."
            ),
        }

        narration = self.narrator.narrate_event(world=world, actor=actor, event=event)
        print("\n" + "─" * 90)
        print(narration)
        print("─" * 90 + "\n")
