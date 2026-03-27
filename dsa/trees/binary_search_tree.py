class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order_traversal(node: Node):
    if not node:
        return

    if node.left:
        in_order_traversal(node.left)

    print(node.val, end=" ")

    if node.right:
        in_order_traversal(node.right)    

# Tree Structure:
#          15
#       /       \
#      10       18
#     /  \     /   \
#    4   11   16   20
 
root = Node(15)

def insert(root, key):
    if root is None:
        return Node(key)
    
    if root.val == key:
        return root
    
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    
    return root

root = insert(root, 10)

print("In Order Tree Traversal: ")
in_order_traversal(root)
print(end="\n")

print("Adding 18", end="\n")
root = insert(root, 18)

print("In Order Tree Traversal: ")
in_order_traversal(root)
print(end="\n")

print("Adding 4", end="\n")
root = insert(root, 4)

print("In Order Traversal: ")
in_order_traversal(root)
print(end="\n")

print("Adding 11", end="\n")
root = insert(root, 11)

print("In Order Traversal: ")
in_order_traversal(root)
print(end="\n")

def search(root, key):
    if not root:
        return False

    if root.val == key:
        return True
    
    if root.val < key:
        return search(root.right, key)
    
    else:
        return search(root.left, key)
    
val = 11
isFound = search(root, val)

print(f"Searching through the Tree for value: {val}")
if isFound:
    print(f"{val} is presented in the Tree")
else:
    print(f"{val} is not presented in the Tree")

# todo:
# need to perform the delete operation