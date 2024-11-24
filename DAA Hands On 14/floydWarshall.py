def floyd_warshall_algorithm(network):
    # Extract all nodes from the graph
    vertices = list(network.keys())
    vertex_indices = {vertex: index for index, vertex in enumerate(vertices)}
    num_vertices = len(vertices)

    # Initialize matrices for shortest paths and next vertices
    min_distances = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    next_vertex = [[None] * num_vertices for _ in range(num_vertices)]

    # Set distance from each vertex to itself as zero
    for idx in range(num_vertices):
        min_distances[idx][idx] = 0

    # Populate initial distances based on edges in the graph
    for origin in network:
        for destination, cost in network[origin]:
            i, j = vertex_indices[origin], vertex_indices[destination]
            min_distances[i][j] = cost
            next_vertex[i][j] = destination

    # Perform the Floyd-Warshall algorithm
    for intermediary in range(num_vertices):
        for source in range(num_vertices):
            for target in range(num_vertices):
                if min_distances[source][intermediary] + min_distances[intermediary][target] < min_distances[source][target]:
                    min_distances[source][target] = min_distances[source][intermediary] + min_distances[intermediary][target]
                    next_vertex[source][target] = next_vertex[source][intermediary]

    return min_distances, next_vertex, vertices


# Function to display the matrix in a readable format
def display_matrix(matrix, vertices):
    print("    ", "  ".join(vertices))
    for i, row in enumerate(matrix):
        print(f"{vertices[i]:<4}", "  ".join(f"{val if val != float('inf') else '∞':<4}" for val in row))


# Graph representation as an adjacency list
network = {
    'A': [('B', 3), ('C', 5)],
    'B': [('C', 2), ('D', 6)],
    'C': [('B', 1), ('D', 4), ('E', 6)],
    'D': [('E', 2)],
    'E': [('A', 3), ('D', 7)]
}

# Execute the Floyd-Warshall algorithm
min_distances, next_vertex, vertices = floyd_warshall_algorithm(network)

# Print the shortest path distance matrix
print("Shortest Path Distance Matrix:")
display_matrix(min_distances, vertices)
