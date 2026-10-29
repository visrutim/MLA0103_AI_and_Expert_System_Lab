"""Experiment 9: Water Jug Problem using BFS.
Finds a sequence of states to measure the target amount.
State = (water in jug A, water in jug B).
"""

from collections import deque
from math import gcd

def water_jug(cap_a, cap_b, target):
    if target < 0 or target > max(cap_a, cap_b) or (target and target % gcd(cap_a, cap_b)):
        return None
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (a, b), path = queue.popleft()
        if a == target or b == target:
            return path
        next_states = [
            (cap_a, b), (a, cap_b), (0, b), (a, 0),
            (a - min(a, cap_b - b), b + min(a, cap_b - b)),
            (a + min(b, cap_a - a), b - min(b, cap_a - a))
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None

if __name__ == "__main__":
    cap_a, cap_b, target = 4, 3, 2
    result = water_jug(cap_a, cap_b, target)
    if result:
        print(f"Jugs: A={cap_a}L, B={cap_b}L; target={target}L")
        for step, state in enumerate(result):
            print(f"Step {step}: Jug A={state[0]}L, Jug B={state[1]}L")
    else:
        print("Target cannot be measured with these jug capacities.")
