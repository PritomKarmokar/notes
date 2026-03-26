class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tree Structure
#         1
#     /       \
#     2         3
#  /    \     /   \
# 4      5   6     7
# 

nodeOne = Node(1)
nodeTwo = Node(2)
nodeThree = Node(3)
nodeFour = Node(4)
nodeFive = Node(5)
nodeSix = Node(6)
nodeSeven = Node(7)

root = nodeOne
root.left = nodeTwo
root.right = nodeThree

nodeTwo.left = nodeFour
nodeTwo.right = nodeFive

nodeThree.left = nodeSix
nodeThree.right = nodeSeven

# Tree Traversal

def bfs(root: Node):
    # Level Order Traversal using Queue Concept
    if not root:
        return
    
    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0) # pop(0) to achieve FIFO order

        print(current_node.value, end=" ")

        if current_node.left:
            queue.append(current_node.left)
        
        if current_node.right:
            queue.append(current_node.right)
    
    print()

def dfs(root: Node):
    # DFS implementation using Stack Concept, Not Recursion
    if not root:
        return
    
    stack = []
    stack.append(root)

    while stack:
        current_node = stack.pop() # pop to achieve LIFO order

        print(current_node.value, end=" ")
        
        if current_node.left:
            stack.append(current_node.left)
        
        if current_node.right:
            stack.append(current_node.right)
        
    print()

print("Tree Traversal(BFS):")
bfs(root)
print()

print("Tree Traversal(DFS):")
dfs(root)
print()

# There is also Recursive Version of DFS Traversal
# Recursive DFS has three variants.
# 01. Pre Order 02. In Order 03. Post Order

# Pre Order: Root -> Left -> Right

def pre_order(node: Node):
    if not node:
        return
    
    print(node.value, end=" ")

    if node.left:
        pre_order(node.left)
    
    if node.right:
        pre_order(node.right)

# In Order: Left -> Root -> Right
def in_order(node: Node):
    if not node:
        return
    
    if node.left:
        in_order(node.left)

    print(node.value, end=" ")

    if node.right:
        in_order(node.right)
    

# Post Order: Left -> Right -> Root
def post_order(node: Node):
    if not node:
        return
    
    if node.left:
        post_order(node.left)
    
    if node.right:
        post_order(node.right)
    
    print(node.value, end=" ")


print("Recursive DFS Traversal", end="\n\n")

print("Pre Order Traversal:")
pre_order(root)
print()

print("In Order Traversal:")
in_order(root)
print()

print("Post Order Traversal:")
post_order(root)
print()