"""
recursive pre-order

pre-order from top to left then right

recursive vs iterative
"""
from TreeDSA import BinaryTree


def Recursive_Pre_Ord(root):
    if root is None:
        return

    print(' ', root.data)
    Recursive_Pre_Ord(root.left)
    Recursive_Pre_Ord(root.right)


newTree = BinaryTree()
newTree.createBinaryTree()
print("from Recursive_Pre_Ord: ", Recursive_Pre_Ord(newTree.root))


def Regular_Pre_Ord(root):
    if root is None:
        return

    stack = [root]
    ans = []
    while stack:
        currNode = stack.pop()
        ans.append(currNode.data)

        if currNode.left: stack.append(currNode.left)
        if currNode.right: stack.append(currNode.right)

    print(ans)


print(Regular_Pre_Ord(newTree.root))


