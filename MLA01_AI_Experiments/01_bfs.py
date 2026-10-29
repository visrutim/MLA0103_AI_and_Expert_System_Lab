"""Experiment 1: Breadth First Search (BFS)
Finds a shortest path in an unweighted graph.
"""
from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
        "D": [], "E": ["G"], "F": ["G"], "G": []
    }
    start, goal = "A", "G"
    path = bfs_shortest_path(graph, start, goal)
    print("BFS shortest path:", " -> ".join(path) if path else "No path found")
