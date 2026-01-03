from collections import deque
from Task1 import create_transport_graph

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = path + [neighbor]
                queue.append(new_path)

def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    if start == goal:
        return path

    visited.add(start)

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result

    return None

if __name__ == "__main__":
    G = create_transport_graph()

    start = "Central"
    end = "Airport"

    bfs_result = bfs_path(G, start, end)
    dfs_result = dfs_path(G, start, end)

    print("BFS шлях:", bfs_result)
    print("DFS шлях:", dfs_result)