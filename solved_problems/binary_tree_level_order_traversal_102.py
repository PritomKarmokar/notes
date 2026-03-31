class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Generating the Tree part 
nodeThree = Node(3)
nodeNine = Node(9)
nodeTwenty = Node(20)
nodeFifteen = Node(15)
nodeSeven = Node(7)

root = nodeThree

root.left = nodeNine
root.right = nodeTwenty

nodeTwenty.left = nodeFifteen
nodeTwenty.right = nodeSeven

def levelOrder(root):
    if root is None:
        return []
    
    queue = []
    result = []

    queue.append(root)

    while queue:
        current_level = []
        current_length = len(queue)

        for _ in range(current_length):
            current_node = queue.pop(0)
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
        
        result.append(current_level)

    return result

print("BFS Traversal: ")
result = levelOrder(root)
print(result)
