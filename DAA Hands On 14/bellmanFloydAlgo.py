def bellman_ford_algorithm(network, source):
    # Initialize all nodes with infinite distances except the source, which is 0
    min_distances = {vertex: float('inf') for vertex in network}
    min_distances[source] = 0

    # Dictionary to track the predecessor of each vertex in the shortest path
    predecessors = {vertex: None for vertex in network}

    # Extract all edges as a list of (start, end, weight)
    edge_list = [(start, end, cost) for start in network for end, cost in network[start]]

    # Perform |V| - 1 iterations to relax all edges
    for _ in range(len(network) - 1):
        for start, end, cost in edge_list:
            if min_distances[start] + cost < min_distances[end]:
                min_distances[end] = min_distances[start] + cost
                predecessors[end] = start

    # Check for negative weight cycles
    for start, end, cost in edge_list:
        if min_distances[start] + cost < min_distances[end]:
            raise ValueError("The graph contains a negative weight cycle")

    return min_distances, predecessors

# Example graph structure
network = {
    'A': [('B', 3), ('C', 5)],
    'B': [('C', 2), ('D', 6)],
    'C': [('B', 1), ('D', 4), ('E', 6)],
    'D': [('E', 2)],
    'E': [('A', 3), ('D', 7)]
}

# Run the Bellman-Ford algorithm from the source node 'A'
try:
    shortest_distances, path_predecessors = bellman_ford_algorithm(network, 'A')

    # Print the results
    print("Minimum distances from source 'A':")
    for vertex, distance in shortest_distances.items():
        print(f"{vertex}: {distance}")

    print("\nShortest paths from source 'A':")
    for vertex in path_predecessors:
        path = []
        current_vertex = vertex
        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = path_predecessors[current_vertex]
        print(f"Path to {vertex}: {' -> '.join(path)}")
except ValueError as error:
    print(error)
