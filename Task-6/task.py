class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
def print_level(root, level):
    if not root:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        print_level(root.left, level - 1)
        print_level(root.right, level - 1)
def bfs_without_queue(root):
    h = height(root)
    for i in range(1, h + 1):
        print_level(root, i)