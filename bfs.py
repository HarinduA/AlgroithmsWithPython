from collections import deque

def bfs(graph, start):
    visited = set()         # Track visited nodes
    queue = deque([start])  # Use a queue to control traversal order
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(graph[vertex])  # Add neighbors to the queue

    return result

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs_result = bfs(graph, 'A')
print("BFS traversal:", bfs_result)
