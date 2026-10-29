"""Experiment 8: Alpha-Beta pruning applied to a game tree."""

def alpha_beta(tree, maximizing, alpha=float("-inf"), beta=float("inf")):
    if isinstance(tree, (int, float)):
        return tree
    if maximizing:
        value = float("-inf")
        for child in tree:
            value = max(value, alpha_beta(child, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    value = float("inf")
    for child in tree:
        value = min(value, alpha_beta(child, True, alpha, beta))
        beta = min(beta, value)
        if beta <= alpha:
            break
    return value

if __name__ == "__main__":
    game_tree = [
        [3, 5, 2],
        [9, 1, 4],
        [6, 7, 8]
    ]
    print("Best score for MAX with alpha-beta pruning:", alpha_beta(game_tree, True))
