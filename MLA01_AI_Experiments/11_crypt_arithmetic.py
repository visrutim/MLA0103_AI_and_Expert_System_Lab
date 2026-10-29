"""Experiment 11: Crypt-arithmetic puzzle SEND + MORE = MONEY.
Uses backtracking and distinct digits for letters.
"""

from itertools import permutations

def solve_send_more_money():
    letters = "SENDMORY"
    for digits in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, digits))
        if mapping["S"] == 0 or mapping["M"] == 0:
            continue
        send = 1000*mapping["S"] + 100*mapping["E"] + 10*mapping["N"] + mapping["D"]
        more = 1000*mapping["M"] + 100*mapping["O"] + 10*mapping["R"] + mapping["E"]
        money = 10000*mapping["M"] + 1000*mapping["O"] + 100*mapping["N"] + 10*mapping["E"] + mapping["Y"]
        if send + more == money:
            return mapping, send, more, money
    return None

if __name__ == "__main__":
    solution = solve_send_more_money()
    if solution:
        mapping, send, more, money = solution
        print("Solution: SEND + MORE = MONEY")
        print(f"{send} + {more} = {money}")
        print("Letter-digit mapping:", mapping)
    else:
        print("No solution found.")
