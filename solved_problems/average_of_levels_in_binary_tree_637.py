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

def averageOfLevels(root):
    if root is None:
        return []
    
    result = []
    queue = []
    queue.append(root)

    while queue:
        current_level_sum = 0
        current_length = len(queue)

        for _ in range(current_length):
            current_node = queue.pop(0)
            current_level_sum += current_node.val

            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
        
        current_level_avg = current_level_sum / current_length
        result.append(current_level_avg)

    return result

result = averageOfLevels(root)
print(f"result: {result}")