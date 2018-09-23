#!/usr/bin/python3

# Binary trees are trees with only two nodes

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    # inoder stands for processing the current node in the traversal
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    # preorder statnds for processing the current node before traversal
    if root is None:
        return
    print(root.val)
    inorder(root.left)
    inorder(root.right)

def postorder(root):
    # postorder stands for processing the current node after the traversal
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.val)


