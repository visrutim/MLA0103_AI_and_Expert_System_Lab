"""Experiment 20: Person DOB Knowledge Base."""

from datetime import date

PEOPLE = {
    "Asha": "2005-04-12",
    "Rahul": "2004-11-03",
    "Maya": "2006-01-25",
}

def get_dob(name):
    dob_text = PEOPLE.get(name.strip().title())
    return date.fromisoformat(dob_text) if dob_text else None

if __name__ == "__main__":
    name = input("Enter a sample name (Asha/Rahul/Maya): ")
    dob = get_dob(name)
    if dob:
        print(f"{name.title()}'s date of birth is {dob.strftime('%d-%m-%Y')}")
    else:
        print("Name not found in the sample knowledge base.")
