"""
Binary Search Tree

a type of tree in which data is organized in an ordered manner.
helps with faster search and insertion of data.
it satisfies the following properties:
  1) the left subtree of a node contains only nodes with values < root node
  2) the right subtree of a node contains only nodes with values > root node
  3) the left and right subtree each must also be a binary search tree

  ex:

                                5
                            3       7     <-- this is a binary search tree
                        2    4    6   8
                    1


  ex NOT:
                                6
                            4       8     <-- this is NOT! a binary search tree
                        2    8    5   9
                  because 8 on the left is larger than 6
                  and 5 is less than 6 and is on the right

"""
from TreeDSA import BinaryTree, TreeNode


def Num_Exist_in_BST(root, num):
    if root is None:
        return False

    stack = [root]
    while stack:
        current = stack.pop()

        if current.data == num: return True
        if current.data > num and current.left: stack.append(current.left)
        if current.data < num and current.right: stack.append(current.right)
    return False


def find_Target_BST(root, num):
    if root is None:
        return False

    stack = [root]
    while stack:
        curr = stack.pop()
        print("curr.data: ", curr.data)
        if num == curr.data: return True
        if num < curr.data and curr.left: stack.append(curr.left)
        if num > curr.data and curr.right: stack.append(curr.right)

    return False


def isValid(root):

    def valid(right, node, left):
        if node is None:
            return True

        if not (right > node.data > left):
            return False

        return valid(node.data, node.left, left) and \
            valid(right, node.right, node.data)

    return valid(float('inf'), root, float('-inf'))


newTree = BinaryTree()
newTree.createBinaryTree()

newTree2 = BinaryTree()
newTree2.root = TreeNode(5)
newTree2.root.left = TreeNode(9)
newTree2.root.right = TreeNode(3)

newTree3 = BinaryTree()
newTree3.root = TreeNode(2)
newTree3.root.left = TreeNode(1)
newTree3.root.right = TreeNode(3)

print(isValid(newTree.root))
print(isValid(newTree2.root))
print(isValid(newTree3.root))
