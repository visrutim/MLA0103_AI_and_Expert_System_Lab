"""Experiment 17: Rule-based Medical Expert System.
Educational demonstration only; not a diagnosis."""

RULES = [
    ({"fever", "cough"}, "Possible respiratory infection pattern"),
    ({"fever", "body pain"}, "Possible flu-like illness pattern"),
    ({"sneezing", "runny nose"}, "Possible allergy or common-cold pattern"),
    ({"headache", "fever"}, "Fever with headache needs clinical context"),
]

def infer(symptoms):
    symptoms = {s.strip().lower() for s in symptoms if s.strip()}
    matches = [conclusion for required, conclusion in RULES if required <= symptoms]
    return matches or ["No matching rule; consult a qualified healthcare professional if concerned."]

if __name__ == "__main__":
    entered = input("Enter symptoms separated by commas: ")
    print("Rule-based results (not a diagnosis):")
    for conclusion in infer(entered.split(",")):
        print("-", conclusion)
    print("Seek urgent care for severe or rapidly worsening symptoms.")
