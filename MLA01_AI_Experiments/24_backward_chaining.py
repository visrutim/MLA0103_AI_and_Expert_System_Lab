"""Experiment 24: Backward Chaining goal-driven reasoning."""

RULES = {
    "possible_infection": [{"has_fever", "has_cough"}],
    "infection_supported": [{"possible_infection", "test_positive"}],
    "possible_allergy_or_cold": [{"has_sneezing", "has_runny_nose"}],
}

def backward_chain(goal, facts, active=None):
    facts = set(facts)
    active = set() if active is None else active
    if goal in facts:
        return True
    if goal in active or goal not in RULES:
        return False
    active.add(goal)
    for conditions in RULES[goal]:
        if all(backward_chain(condition, facts, active.copy()) for condition in conditions):
            return True
    return False

if __name__ == "__main__":
    entered = input("Enter known facts separated by commas: ")
    facts = {fact.strip().lower() for fact in entered.split(",") if fact.strip()}
    goal = input("Enter goal to prove (e.g. possible_infection): ").strip().lower()
    print("Goal proven." if backward_chain(goal, facts) else "Goal cannot be proven from the current facts.")
