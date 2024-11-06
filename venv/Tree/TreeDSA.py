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

Types of binary trees:

complete binary tree:                       full binary tree:
        1                                            1
    2       3                                  2          3
4      5  6   7                            4     5      6     7
8                                        8  9  10 11  12 13  14 15
complete is full at all levels          full is complete at all levels
except the last                         including the last


DFS --> there are three different ways: pre-order, in-order and post-order
    Pre-order Traversal:
    displaying the current node and traversing left
    print all left until no more, then print right.

    In-order Traversal:
    display the left hen when there are no more left
    display the middle + root and then all right values.

    Pre-order Traversal:
    display all left then all right then root

BFS -->


Level-Order Travesal:
        print all levels in order so 12345678
        we use a queue add everything to the queue. add 1
        print it find its children: 2,3  into the queue print 2 find 2s children
        add 4,5 to the queue. pop the queue print 3 and find 3 children
        add to queue 3 has no children so move on to next in queue: 4
        print 4 and check for children it has none
        print 5 and find 5 children has none no more queue and no more elements
        return

"""


def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node.data)
    in_order(node.right)


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


class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None


# def Level_Order(node):
#     if not node:
#         return
#     queue = [node]
#     traversal = ""
#     # while queue:



tree1 = BinaryTree()
tree1.createBinaryTree()
# print(Level_Order(tree1.root))



