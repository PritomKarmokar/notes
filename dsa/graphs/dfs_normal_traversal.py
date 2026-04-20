from collections import deque

# -----------------------------
# GRAPH INPUT (Adjacency List)
# -----------------------------

graph = {}


# Input:
# First line: number of nodes and edges
nodes, edges = map(int, input("Enter nodes and edges: ").split())

# Next 'edges' lines: each line contains an undirected edge (u, v)
for _ in range(edges):
    u, v = map(int, input("Enter edge (u, v): ").split())

    # Initialize adjacency list if node not present
    if u not in graph:
        graph[u] = []
    
    if v not in graph:
        graph[v] = []

    # Since this is an undirected graph, add both ways
    graph[u].append(v)
    graph[v].append(u)


# Sample Input:
#   5 5
#   1 2
#   1 4
#   2 3
#   2 5
#   3 5

# -----------------------------
# PRINT GRAPH
# -----------------------------
print("Adjacency List Representation: ")
for node, neighbors in graph.items():
    print(f"{node} --> {neighbors}")


# -----------------------------
# DEPTH FIRST SEARCH (DFS)
# -----------------------------

def dfs(root):
    """
    Iterative DFS using stack.

    Key Idea:
    - Use stack (LIFO)
    - Visit a node
    - Push its unvisited neighbors
    """

    visited = set()
    stack = deque()
    
    visited.add(root)
    stack.append(root)

    print("DFS Traversal: ")

    while stack:
        current = stack.pop()

        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    
    print(end="\n")


dfs(1)