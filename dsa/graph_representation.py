# Graph Representation: for directed unweighted graph. Taking input from user (Instead of Files)

# Adjacency Matrix Representation
# graph = [
#     [0, 1, 1, 0, 0],
#     [0, 0, 0, 1, 1],
#     [0, 0, 0, 1, 0],
#     [1, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0]
# ]

# Adjacency List Representation
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['D'],
#     'D': ['E', 'A'],
#     'E': []
# }

graph = dict()

def addEdge(node1, node2):
    if node1 not in graph:
        graph[node1] = []
    
    if node2 not in graph:
        graph[node2] = []
    
    graph[node1].append(node2)

    # for bidirectional graph
    # graph[node2].append(node1)

def main():
    _, edges = input().split()

    for _ in range(int(edges)):
        node1, node2 = input().split()
        addEdge(node1, node2)
    
    for key, val in graph.items():
        print(f"{key} --> {val}")


if __name__ == "__main__":
    main()