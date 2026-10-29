"""Experiment 3: Uniform Cost Search (UCS)
Finds a least-cost path in a weighted graph with non-negative costs.
"""
import heapq
from itertools import count

def uniform_cost_search(graph, start, goal):
    tie = count()
    frontier = [(0, next(tie), start, [start])]
    best_cost = {start: 0}
    while frontier:
        cost, _, node, path = heapq.heappop(frontier)
        if cost != best_cost.get(node):
            continue
        if node == goal:
            return path, cost
        for neighbor, edge_cost in graph.get(node, {}).items():
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, next(tie), neighbor, path + [neighbor]))
    return None, float("inf")

if __name__ == "__main__":
    graph = {
        "A": {"B": 2, "C": 5}, "B": {"C": 1, "D": 4},
        "C": {"D": 1}, "D": {}
    }
    path, cost = uniform_cost_search(graph, "A", "D")
    print("Path:", " -> ".join(path) if path else "No path found")
    print("Total cost:", cost if path else "N/A")
