"""Experiment 7: Minimax algorithm for a small game tree.
Leaves are example utility scores from the maximizing player's perspective.
"""

def minimax(tree, maximizing):
    if isinstance(tree, (int, float)):
        return tree
    values = [minimax(child, not maximizing) for child in tree]
    return max(values) if maximizing else min(values)

if __name__ == "__main__":
    game_tree = [
        [3, 5, 2],   # opponent chooses minimum: 2
        [9, 1, 4],   # opponent chooses minimum: 1
        [6, 7, 8]    # opponent chooses minimum: 6
    ]
    print("Best score for MAX:", minimax(game_tree, True))
