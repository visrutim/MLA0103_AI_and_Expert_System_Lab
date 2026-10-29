"""Experiment 15: Family Knowledge Representation using logical rules."""

parents = {
    ("Ravi", "Anu"), ("Ravi", "Kiran"),
    ("Meena", "Anu"), ("Meena", "Kiran"),
    ("Anu", "Diya"), ("Arun", "Diya")
}

def is_parent(parent, child):
    return (parent, child) in parents

def children_of(parent):
    return sorted(child for p, child in parents if p == parent)

def siblings(person):
    person_parents = {p for p, child in parents if child == person}
    result = set()
    for p, child in parents:
        if p in person_parents and child != person:
            result.add(child)
    return sorted(result)

def grandparents_of(person):
    grandparents = set()
    for parent, child in parents:
        if child == person:
            grandparents.update(p for p, grandchild in parents if grandchild == parent)
    return sorted(grandparents)

if __name__ == "__main__":
    person = input("Enter a person (try Diya or Anu): ").strip()
    print("Parents:", sorted(p for p, child in parents if child == person))
    print("Children:", children_of(person))
    print("Siblings:", siblings(person))
    print("Grandparents:", grandparents_of(person))
