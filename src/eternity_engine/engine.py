from cultivators import Cultivator

def start_simulation():
    cultivator = Cultivator(name="Li Ming")
    print(f"Simulation started for: {cultivator.name}")

if __name__ == "__main__":
    start_simulation()