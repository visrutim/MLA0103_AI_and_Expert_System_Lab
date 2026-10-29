"""Experiment 18: Fruit Color Classification using production rules."""

def classify_fruit(color):
    color = color.strip().lower()
    rules = {
        "red": ["apple", "strawberry", "cherry"],
        "orange": ["orange", "papaya"],
        "yellow": ["banana", "lemon"],
        "green": ["lime", "green apple"],
        "purple": ["grape", "plum"],
    }
    return rules.get(color, [])

if __name__ == "__main__":
    color = input("Enter fruit color (red/orange/yellow/green/purple): ")
    fruits = classify_fruit(color)
    if fruits:
        print(f"Possible fruits with {color.lower()} color:", ", ".join(fruits))
    else:
        print("No rule found for that color.")
