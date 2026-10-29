"""Experiment 16: Birds Fly Knowledge Base with exceptions."""

birds = {"sparrow", "pigeon", "parrot", "eagle", "penguin", "ostrich"}
cannot_fly = {"penguin", "ostrich"}

def can_fly(animal):
    animal = animal.strip().lower()
    if animal not in birds:
        return None
    return animal not in cannot_fly

if __name__ == "__main__":
    animal = input("Enter a bird name: ")
    result = can_fly(animal)
    if result is None:
        print("Knowledge base has no information about that animal.")
    elif result:
        print(f"Rule-based conclusion: {animal.lower()} can fly.")
    else:
        print(f"Exception rule: {animal.lower()} cannot fly.")
