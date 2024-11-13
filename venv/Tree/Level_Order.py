"""

when ww have a BST we can print out the numbers in order



                  5
              3      7     <-- this is a binary tree
            2   4    6  8
          1
"""
from collections import deque

from TreeDSA import BinaryTree


def lvlOrder(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)  #
    arr = []
    while queue:
        current = queue.popleft()

        arr.append(current.data)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return arr


def Reverse_lvlOrder(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)  #
    arr = []
    while queue:
        current = queue.popleft()

        arr.append(current.data)
        if current.right: queue.append(current.right)
        if current.left: queue.append(current.left)

    return arr


def calculate_height_of_tree(root):
    if root is None:
        return -1

    stack = [root]
    total = 0
    while stack:
        current = stack.pop()
        total += 1
        if current.left:
            stack.append(current.left)
            total += 1
        if current.right:
            stack.append(current.right)
            total += 1

    return round(total / 4)


def calculate_height_of_tree_Recursive(root):
    if root is None:
        return -1

    leftHeight = calculate_height_of_tree_Recursive(root.left)
    rightHeight = calculate_height_of_tree_Recursive(root.right)
    return 1 + max(leftHeight, rightHeight)


def Size_of_Tree_Recursive(root):
    if root is None:
        return 0

    leftSize = Size_of_Tree_Recursive(root.left)
    rightSize = Size_of_Tree_Recursive(root.right)

    return 1 + leftSize + rightSize


def Size_of_Tree(root):
    if root is None:
        return 0

    stack = [root]
    size = 1
    while stack:
        current = stack.pop()

        if current.left:
            stack.append(current.left)
            size += 1
        if current.right:
            stack.append(current.right)
            size += 1
    return size


newTree = BinaryTree()
newTree.createBinaryTree()
print(calculate_height_of_tree_Recursive(newTree.root))
print(calculate_height_of_tree(newTree.root))
print(Size_of_Tree_Recursive(newTree.root))
print(Size_of_Tree(newTree.root))

