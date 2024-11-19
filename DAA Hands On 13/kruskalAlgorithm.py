class GraphEdge:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end

class DisjointSetUnion:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_mst(vertices, edges):
    edges = sorted(edges, key=lambda edge: edge.weight)
    dsu = DisjointSetUnion(vertices)
    mst_result = []

    for edge in edges:
        if dsu.find(edge.start) != dsu.find(edge.end):
            dsu.union(edge.start, edge.end)
            mst_result.append(edge)

    return mst_result

# Define nodes and edges for Kruskal's example
nodes_kruskal = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
edges_kruskal = [
    GraphEdge(4, "a", "b"),
    GraphEdge(8, "a", "h"),
    GraphEdge(8, "b", "c"),
    GraphEdge(11, "b", "h"),
    GraphEdge(7, "c", "d"),
    GraphEdge(4, "c", "f"),
    GraphEdge(2, "c", "i"),
    GraphEdge(6, "c", "g"),
    GraphEdge(9, "d", "e"),
    GraphEdge(14, "d", "f"),
    GraphEdge(10, "e", "f"),
    GraphEdge(2, "f", "g"),
    GraphEdge(1, "g", "h"),
    GraphEdge(7, "h", "i")
]

# Perform Kruskal's MST
mst = kruskal_mst(nodes_kruskal, edges_kruskal)
print("Kruskal's MST:")
for edge in mst:
    print(f"Edge {edge.start}-{edge.end} with weight {edge.weight}")
