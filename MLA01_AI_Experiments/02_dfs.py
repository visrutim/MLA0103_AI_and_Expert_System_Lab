"""Experiment 2: Depth First Search (DFS) with backtracking."""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))
    return order

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
        "D": [], "E": [], "F": []
    }
    print("DFS traversal:", " -> ".join(dfs(graph, "A")))
