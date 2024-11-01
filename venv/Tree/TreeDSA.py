"""
it's a non-linear data structure use for storing data
* it is made up of nodes and edges without having any cycle
* each node in a tree can point to n number of nodes in a tree
* it is a way of representing hierarchical structure with a parent node
called as root node and many levels of additional nodes
                1
            2   9   3     <-- this is a regular tree
          4  5     6  7

* leaf nodes are nodes that have no children

*binary tree:
a tree is called as Binary tree if each node has zero, one or two children.
                1
            2      3     <-- this is a binary tree
          4  5     6  7

a binary tree's structure looks like this:
null <-- left <-- data --> right--> null      <-- a TreeNode looks like this
a binary tree is represented by a tree node

basic tree node:

"""


def reversalPreOrder(root):
    if root is None:
        return

    print(root.data, ' ')
    reversalPreOrder(root.left)
    reversalPreOrder(root.right)


def reversalInOrder(root):
    if root is None:
        return

    reversalInOrder(root.left)
    print(root.data, ' ')
    reversalInOrder(root.right)


def reversalPostOrder(root):
    if root is None:
        return

    reversalPostOrder(root.left)
    reversalPostOrder(root.right)
    print(root.data, ' ')


def reversalPreOrder_stack(root):
    if root is None:
        return

    stack = [root]
    while stack:
        temp = stack.pop()
        print(temp.data)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)


def reversalInOrder_stack(root):
    if root is None:
        return

    stack = []  #
    # printed   1 2 3 4 5 6 7 8
    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data, " ")
            curr = curr.right


def reversalPostOrder_stack(root):
    if root is None:
        return

    stack = []
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if not temp:
                temp = stack.pop()
                print(temp.data, " ")
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    print(temp.data, " ")
            else:
                curr = temp


class BinaryTree:
    root = None

    def __init__(self, root_=None):
        self.root = root_

    def createBinaryTree(self):
        rootNode = TreeNode(5)
        left = TreeNode(3)
        right = TreeNode(7)
        left_left = TreeNode(2)
        left_right = TreeNode(4)
        right_left = TreeNode(6)
        right_right = TreeNode(8)
        left_last_val = TreeNode(1)

        self.root = rootNode
        rootNode.left = left
        rootNode.right = right

        left.left = left_left
        left.right = left_right
        left_left.left = left_last_val

        right.left = right_left
        right.right = right_right


"""
                                    5 root
                    (left)3                           7(right)
        (left.left)2     4(left.right)   (right.left)6     8(right.right)
(left.left.left)1       
"""


class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None


tree1 = BinaryTree()
tree1.createBinaryTree()
# reversalPreOrder(tree1.root)
# print("<--reversalPreOrder____________________________reversalPostOrder-->")
reversalPostOrder(tree1.root)
# print("____________________________ reversalInOrder_stack-->")
# reversalInOrder_stack(tree1.root)
# print("____________________________ reversalInOrder-->")
# reversalInOrder(tree1.root)
print("____________________________ reversalPostOrder stack-->")
# reversalPreOrder_stack(tree1.root)
reversalPostOrder_stack(tree1.root)
