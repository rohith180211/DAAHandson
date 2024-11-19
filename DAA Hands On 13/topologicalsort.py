from collections import defaultdict

class DirectedGraph:
    def __init__(self, vertex_count):
        self.adjacency_list = defaultdict(list)
        self.num_vertices = vertex_count

    def insert_edge(self, start, end):
        self.adjacency_list[start].append(end)

    def topological_sort_helper(self, node, visited_nodes, sorted_nodes):
        visited_nodes[node] = True
        for neighbor in self.adjacency_list[node]:
            if not visited_nodes[neighbor]:
                self.topological_sort_helper(neighbor, visited_nodes, sorted_nodes)
        sorted_nodes.insert(0, node)

    def compute_topological_sort(self, vertices):
        visited_nodes = {vertex: False for vertex in vertices}
        sorted_nodes = []
        for vertex in vertices:
            if not visited_nodes[vertex]:
                self.topological_sort_helper(vertex, visited_nodes, sorted_nodes)
        return sorted_nodes

# Define vertices and edges for the example
vertices = ["undershorts", "pants", "belt", "shirt", "tie", "jacket", "socks", "shoes", "watch"]

# List of directed edges
connections = [
    ("undershorts", "pants"),
    ("pants", "belt"),
    ("pants", "shoes"),
    ("shirt", "belt"),
    ("shirt", "tie"),
    ("tie", "jacket"),
    ("belt", "jacket"),
    ("socks", "shoes")
]

# Create graph and add edges
graph = DirectedGraph(len(vertices))
for start, end in connections:
    graph.insert_edge(start, end)

# Perform topological sort
print("Topological Sort:", graph.compute_topological_sort(vertices))
