"""Experiment 19: Planet Knowledge Representation and queries."""

PLANETS = {
    "mercury": {"order": 1, "type": "terrestrial", "moons": 0},
    "venus": {"order": 2, "type": "terrestrial", "moons": 0},
    "earth": {"order": 3, "type": "terrestrial", "moons": 1},
    "mars": {"order": 4, "type": "terrestrial", "moons": 2},
    "jupiter": {"order": 5, "type": "gas giant", "moons": 0}, # simplified example data
    "saturn": {"order": 6, "type": "gas giant", "moons": 0},
    "uranus": {"order": 7, "type": "ice giant", "moons": 0},
    "neptune": {"order": 8, "type": "ice giant", "moons": 0},
}

def query_planet(name):
    return PLANETS.get(name.strip().lower())

if __name__ == "__main__":
    name = input("Enter a planet name: ")
    data = query_planet(name)
    if data:
        print(f"Planet: {name.title()}")
        print("Order from Sun:", data["order"])
        print("Classification:", data["type"])
        print("Known moons (sample data):", data["moons"])
        print("Note: moon counts are placeholders in this simple knowledge-base example.")
    else:
        print("Unknown planet. Please enter one of the eight planets.")
