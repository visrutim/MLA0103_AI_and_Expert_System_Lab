"""Experiment 27: Vowel Identification using rule-based logic."""

def identify_vowels(sentence):
    vowels = "aeiou"
    found = []
    for character in sentence.lower():
        if character in vowels:
            found.append(character)
    return found

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    found = identify_vowels(sentence)
    print("Vowels found:", found)
    print("Total vowels:", len(found))
