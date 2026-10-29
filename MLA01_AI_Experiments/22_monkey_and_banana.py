"""Experiment 22: Monkey and Banana Problem using state-space BFS.
State: (monkey_position, box_position, has_banana).
Positions are floor, middle, and under_banana.
"""

from collections import deque

def solve():
    start = ("floor", "middle", False)
    goal = ("under_banana", "under_banana", True)
    actions = {
        ("floor", "middle", False): [
            ("walk to box", ("middle", "middle", False)),
        ],
    }
    # Generate legal transitions for all states.
    def successors(state):
        monkey, box, has = state
        if has:
            return []
        result = []
        positions = {"floor", "middle", "under_banana"}
        # Monkey may walk if not carrying/holding banana.
        for pos in positions:
            if pos != monkey:
                result.append((f"walk from {monkey} to {pos}", (pos, box, has)))
        # Push box only if monkey is at box and both move to a neighboring position.
        if monkey == box:
            for pos in positions:
                if pos != box:
                    result.append((f"push box from {box} to {pos}", (pos, pos, has)))
        # Climb box only under banana and box is there.
        if monkey == "under_banana" and box == "under_banana":
            result.append(("climb box and grab banana", (monkey, box, True)))
        return result

    queue = deque([(start, [])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for action, new_state in successors(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [action]))
    return None

if __name__ == "__main__":
    plan = solve()
    print("Monkey and Banana plan:")
    if plan:
        for i, action in enumerate(plan, 1):
            print(f"{i}. {action}")
    else:
        print("No plan found.")
