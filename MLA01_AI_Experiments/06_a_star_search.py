"""Experiment 6: A* Search: f(n) = g(n) + h(n)."""

import heapq
from itertools import count

def a_star_search(graph, heuristic, start, goal):
    tie = count()
    frontier = [(heuristic.get(start, 0), next(tie), 0, start, [start])]
    best_g = {start: 0}
    while frontier:
        _, _, g_cost, node, path = heapq.heappop(frontier)
        if g_cost != best_g.get(node):
            continue
        if node == goal:
            return path, g_cost
        for neighbor, edge_cost in graph.get(node, {}).items():
            new_g = g_cost + edge_cost
            if new_g < best_g.get(neighbor, float("inf")):
                best_g[neighbor] = new_g
                f_cost = new_g + heuristic.get(neighbor, 0)
                heapq.heappush(frontier, (f_cost, next(tie), new_g, neighbor, path + [neighbor]))
    return None, float("inf")

if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4}, "B": {"C": 2, "D": 5},
        "C": {"D": 1}, "D": {}
    }
    heuristic = {"A": 4, "B": 3, "C": 1, "D": 0}
    path, cost = a_star_search(graph, heuristic, "A", "D")
    print("A* path:", " -> ".join(path) if path else "No path found")
    print("Total cost:", cost if path else "N/A")
