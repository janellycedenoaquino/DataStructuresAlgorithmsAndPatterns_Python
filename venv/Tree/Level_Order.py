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
        return 0

    leftHeight = calculate_height_of_tree(root.left)
    rightHeight = calculate_height_of_tree(root.right)
    print("print from left:", leftHeight)
    return max(leftHeight, rightHeight) + 1


newTree = BinaryTree()
newTree.createBinaryTree()

