"""Experiment 4: Best First Search using a heuristic priority."""

import heapq
from itertools import count

def best_first_search(graph, heuristic, start, goal):
    tie = count()
    frontier = [(heuristic.get(start, 0), next(tie), start, [start])]
    visited = set()
    while frontier:
        _, _, node, path = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristic.get(neighbor, 0), next(tie), neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": ["G"], "G": []}
    heuristic = {"A": 7, "B": 5, "C": 4, "D": 6, "E": 2, "F": 1, "G": 0}
    path = best_first_search(graph, heuristic, "A", "G")
    print("Best-first path:", " -> ".join(path) if path else "No path found")
