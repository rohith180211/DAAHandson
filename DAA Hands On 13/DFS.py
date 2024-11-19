from collections import defaultdict

def perform_dfs(edges, start_point):
    adjacency_map = defaultdict(list)
    for origin, destination in edges:
        adjacency_map[origin].append(destination)

    seen = set()

    def traverse(node):
        if node not in seen:
            print(node, end=' ')
            seen.add(node)
            for adjacent in adjacency_map[node]:
                traverse(adjacent)

    traverse(start_point)
    print()

# Define edges for DFS example
example_edges = [
    ("u", "v"),
    ("u", "x"),
    ("v", "y"),
    ("y", "x"),
    ("x", "v"),
    ("w", "z"),
    ("w", "y"),
    ("z", "z")  # self-loop
]

print("Depth-First Search from 'u':")
perform_dfs(example_edges, 'u')
