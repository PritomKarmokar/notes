# there might other better solution for this problem
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

def zigzagLevelOrder(root):
    if root is None:
        return []
    
    queue = []
    result = []
    queue.append(root)
    counter = 0

    while queue:
        current_level = []
        current_level_length = len(queue)

        for _ in range(current_level_length):
            current_node = queue.pop(0)
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
            
        if counter % 2 != 0:
            current_level.reverse()
        
        result.append(current_level)
        counter += 1
    
    return result

result = zigzagLevelOrder(root)
print(result)
