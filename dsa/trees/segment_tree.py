# Basic Segment Tree Implementation
# with tree construction and range query

class Node:
    def __init__(self, start, end):
        self.val = None
        self.range_start = start
        self.range_end = end
        self.left = None
        self.right = None

def construct_tree(data, start, end):
    if start == end:
        node = Node(start, end)
        node.val = data[start]
        return node
    
    mid = ( start + end ) // 2
    
    node = Node(start, end)
    node.left = construct_tree(data, start, mid)
    node.right = construct_tree(data, mid + 1, end)
    node.val = node.left.val + node.right.val

    return node

def query(node, start, end):
    if node is None:
        return 0

    print(f"Visiting node [{node.range_start}, {node.range_end}] with query [{start}, {end}]")

    if node.range_start >= start and node.range_end <= end:
        return node.val

    if node.range_end < start or node.range_start > end:
        return 0

    return query(node.left, start, end) + query(node.right, start, end)

def pre_order_traversal(node):
    if not node:
        return 
    
    print(node.val, end=" ")

    if node.left:
        pre_order_traversal(node.left)
    
    if node.right:
        pre_order_traversal(node.right)


if __name__ == "__main__":
    data = [3, 4, 9, 12]
    length = len(data)

    print("Constructing Segment Trees : ")
    root = construct_tree(data, 0, length - 1)
    
    print("Segment Tree Traversal: ")
    pre_order_traversal(root)
    print()
    
    result = query(root, 1, 2)
    print(f"result: {result}")