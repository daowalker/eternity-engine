from eternity_engine.infra import get_catalog, ConfigSettings
from eternity_engine.core.cultivators import Cultivator

def main() -> None:
    catalog = get_catalog(ConfigSettings())
    human = catalog.races.get("human")
    demon = catalog.races.get("demon")

    c = Cultivator(name="Soul", age=18, race=human)
    print("Race:", c.race.id, c.race.name)
    print("Absorb Nature?", c.can_absorb_qi("Nature"))
    print("Absorb Demonic?", c.can_absorb_qi("Demonic"))

    print("--------")

    dc = Cultivator(name="Demon Soul", age=18, race=demon)
    print("Race:", dc.race.id, dc.race.name)
    print("Absorb Nature?", dc.can_absorb_qi("Nature"))
    print("Absorb Demonic?", dc.can_absorb_qi("Demonic"))

if __name__ == "__main__":
    main()
