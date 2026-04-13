# Graph Representation: taking input from file `input.txt` for directed, weighted graph
 
graph = dict()

def addEdge(node1, node2, cost):
    if node1 not in graph:
        graph[node1] = []

    if node2 not in graph:
        graph[node2] = []

    graph[node1].append((node2, int(cost)))

def main():
    with open("input.txt") as f:
        lines = f.readlines()

    nodes, edges = lines[0].split()

    for i in range(1, len(lines)):
        node1, node2, cost = lines[i].split()
        addEdge(node1, node2, cost)

    for key, val in graph.items():
        print(f"{key} --> {val}")


if __name__ == "__main__":
    main()