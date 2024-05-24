class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomViewHelper(root, store, hd, level):
    if root is None:
        return 

    # If the horizontal distance is not in store or the current level is deeper
    if hd not in store or store[hd][0] <= level:
        store[hd] = (level, root.data)

    # Recur for left and right subtrees
    bottomViewHelper(root.left, store, hd - 1, level + 1)
    bottomViewHelper(root.right, store, hd + 1, level + 1)

def findBottomView(root):
    result = []
    if root is None:
        return result

    store = {}
    bottomViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result

# Example usage
# Constructing a simple binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
root.right.left = Node(6)

print(findBottomView(root))  # Output should be [4, 2, 5, 3, 6]
