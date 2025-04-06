import heapq

def dijkstra(graph, start):
    # Distance from start to each node (default to infinity)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min-heap: (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we already found a better path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Update distance if found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

shortest_paths = dijkstra(graph, 'A')
print("Shortest paths from A:", shortest_paths)
