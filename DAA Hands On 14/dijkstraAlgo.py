import heapq


def dijkstra_algorithm(network, source):
    # Priority queue to manage (cost, vertex)
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))

    # Dictionary to hold the shortest distance to each vertex
    shortest_distances = {vertex: float('inf') for vertex in network}
    shortest_distances[source] = 0

    # Dictionary to keep track of the path taken
    path_predecessors = {vertex: None for vertex in network}

    while priority_queue:
        current_cost, current_vertex = heapq.heappop(priority_queue)

        # Skip processing if the current cost is greater than the recorded shortest distance
        if current_cost > shortest_distances[current_vertex]:
            continue

        # Check each neighboring vertex
        for neighbor, edge_cost in network[current_vertex]:
            new_cost = current_cost + edge_cost

            # Update if a shorter distance to the neighbor is found
            if new_cost < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_cost
                path_predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return shortest_distances, path_predecessors


# Example network definition
network = {
    'A': [('B', 3), ('C', 5)],
    'B': [('C', 2), ('D', 6)],
    'C': [('B', 1), ('D', 4), ('E', 6)],
    'D': [('E', 2)],
    'E': [('A', 3), ('D', 7)]
}

# Run Dijkstra's algorithm starting from the source vertex 'A'
shortest_distances, path_predecessors = dijkstra_algorithm(network, 'A')

# Print the shortest distances
print("Shortest distances from source 'A':")
for vertex, distance in shortest_distances.items():
    print(f"{vertex}: {distance}")

# Print the paths
print("\nPaths from source 'A':")
for vertex in path_predecessors:
    path = []
    current_vertex = vertex
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = path_predecessors[current_vertex]
    print(f"Path to {vertex}: {' -> '.join(path)}")
