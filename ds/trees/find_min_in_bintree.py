#!/usr/bin/python3


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_min(root, min):
    if not root:
        return min
    # pre-order traversal.
    # Processing the node before traversal. Key point is to set min on traversal
    if root.data < min:
        min = root.data
    min = get_min(root.left, min)
    min = get_min(root.right, min)
    return min


if __name__ == "__main__":
    root = Node(6)
    root.right = Node(4)
    root.left = Node(1)
    root.left.left = Node(7)
    root.right.left = Node(19)
    print(get_min(root, root.data))
