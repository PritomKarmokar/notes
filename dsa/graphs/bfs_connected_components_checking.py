from collections import deque

graph = dict()

# Input:
# First line: number of nodes and edges
nodes, edges = map(int, input("Enter nodes and edges: ").split())

# Next 'edges' lines: each line contains an undirected edge (u, v)
for _ in range(edges):
    u, v = map(int, input("Enter edge(u, v): ").split())

    if u not in graph:
        graph[u] = []
    
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

# Sample Input:
#   5 4
#   1 3
#   1 4
#   3 4
#   2 5

print(end="\n")
print("Adjacency List Representation: ")
for node, neighbor in graph.items():
    print(f"{node} --> {neighbor}")
print(end="\n")

def bfs():
    visited = set()
    connected_components = 0

    def traverse(node):
        queue = deque()
        queue.append(node)

        while queue:
            curr_node = queue.popleft()

            if curr_node in visited:
                continue
            
            visited.add(curr_node)
            for neighbor in graph[curr_node]:
                queue.append(neighbor)
                
    
    for node, neighbor in graph.items():
        for val in neighbor:
            if val not in visited:
                traverse(val)
                connected_components += 1

    return connected_components

result = bfs()
print(f"Number of connected components = {result}")