def dijkstra(graph, start, end):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited_nodes = list(graph.keys())
    previous_nodes = {}

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda vertex: distances[vertex])
        unvisited_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node

    shortest_path = []
    current_node = end
    while current_node != start:
        shortest_path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    shortest_path.insert(0, start)

    return distances[end], shortest_path


graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

for x, y in graph.items():
    print(f"{x}: {y}\n")

start, end = "A", "D"
shortest_distance, shortest_path = dijkstra(graph, start, end)
print(f"Shortest distance from {start} to {end}: {shortest_distance}")
print(f"Shortest path: {' -> '.join(shortest_path)}")
