"""Experiment 23: Forward Chaining inference engine."""

RULES = [
    ({"has_fever", "has_cough"}, "possible_infection"),
    ({"possible_infection", "test_positive"}, "infection_supported"),
    ({"has_sneezing", "has_runny_nose"}, "possible_allergy_or_cold"),
]

def forward_chain(initial_facts):
    facts = set(initial_facts)
    changed = True
    while changed:
        changed = False
        for conditions, conclusion in RULES:
            if conditions <= facts and conclusion not in facts:
                facts.add(conclusion)
                changed = True
    return facts

if __name__ == "__main__":
    entered = input("Enter facts separated by commas (e.g. has_fever,has_cough,test_positive): ")
    facts = {fact.strip().lower() for fact in entered.split(",") if fact.strip()}
    print("Facts and inferred conclusions:")
    for fact in sorted(forward_chain(facts)):
        print("-", fact)
