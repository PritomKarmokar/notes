from collections import deque

# -----------------------------
# GRAPH INPUT (Adjacency List)
# -----------------------------

graph = dict()

# Input:
# First line: number of nodes and edges
nodes, edges = map(int, input("Enter nodes and edges: ").split())

# Next 'edges' lines: each line contains an undirected edge (u, v)
for _ in range(edges):
    u, v = map(int, input("Enter edge(u, v): ").split())

    # Initialize adjacency list if node not present
    if u not in graph:
        graph[u] = []
    
    if v not in graph:
        graph[v] = []
    
    # Since it's an undirected graph, add both connections
    graph[u].append(v)
    graph[v].append(u)

# Sample Input
#   6 6
#   1 2
#   1 4
#   2 3
#   2 5
#   5 6
#   3 6

# -----------------------------
# PRINT GRAPH
# -----------------------------
print("Adjacency List Representation: ")
for node, neighbors in graph.items():
    print(f"{node} --> {neighbors}")

# -----------------------------
# BREADTH FIRST SEARCH (BFS)
# -----------------------------

def bfs(root):
    queue = deque()
    visited = set()
    distance = dict()

    queue.append(root)
    visited.add(root)
    distance[root] = 0

    while queue:
        curr_node = queue.popleft()

        print(curr_node, end=" ")

        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[curr_node] + 1
    
    print(end="\n")

    # Print shortest distances from root
    print("Distance from Root: ")
    for key, val in distance.items():
        print(f"{key} : {val}")
    
    print(end="\n")


# Calling BFS starting from node 1
bfs(1)