# Basic Segment Tree Implementation
# with tree construction and range query

class Node:
    def __init__(self, start, end):
        self.val = None
        self.start = start
        self.end = end
        self.left = None
        self.right = None

def make_segment_tree(data, start, end):
    if start == end:
        leaf = Node(start, end)
        leaf.val = data[start]
        return leaf
    
    mid = (start + end) // 2
    
    node = Node(start, end)
    node.left = make_segment_tree(data, start, mid)
    node.right = make_segment_tree(data, mid + 1, end)
    node.val = node.left.val + node.right.val

    return node

def query(node, qs, qe):
    if node is None:
        return 0
    
    if node.end < qs and node.start > qe:
        return 0
    
    if node.start >= qs and node.end <= qe:
        return node.val
    
    left_sum = query(node.left, qs, qe)
    right_sum = query(node.right, qs, qe)
    
    return left_sum + right_sum

def pre_order_traversal(node):
    if not node:
        return
    
    print(node.val, end=" ")
    
    if node.left:
        pre_order_traversal(node.left)

    if node.right:
        pre_order_traversal(node.right)

if __name__ == "__main__":
    data = [1, 4, 5, 9, 10, 12]
    length = len(data)
    root = make_segment_tree(data, 0, length - 1)

    print("Pre-order traversal of the segment tree:")
    pre_order_traversal(root)
    print(end="\n")

    result = query(root, 2, 4)
    print("Query sum from index 2 to 4:", result)
    result = query(root, 1, 2)
    print(f"result: {result}")
