class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

def hasPathSum(root, targetSum):
    queue = []
    queue.append([root, [root.val]])

    while queue:
        curr_node, curr_path = queue.pop(0)

        if not curr_node.left and not curr_node.right:
            current_path_sum = sum(curr_path)
            if current_path_sum == targetSum:
                return True
        
        if curr_node.left:
            queue.append([curr_node.left, curr_path + [curr_node.left.val]])

        if curr_node.right:
            queue.append([curr_node.right, curr_path + [curr_node.right.val]])

    return False

if hasPathSum(root, 5):
    print("Yes path sum")
else:
    print("No")