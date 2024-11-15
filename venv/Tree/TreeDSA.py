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



a root is a node that has no parents


                                5
                            3       7     <-- this is a binary search tree
                        2    4    6   8
                    1
"""
from collections import deque


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

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return self.root.data

        def _insert_recursive(curr_node, val):
            if curr_node is None:
                return TreeNode(val)

            if val < curr_node.data:
                curr_node.left = _insert_recursive(curr_node.left, val)
            else:
                curr_node.right = _insert_recursive(curr_node.right, val)
            return curr_node

        _insert_recursive(self.root, val)

    def createMaxHeap(self):
        rootNode = TreeNode(9)
        left = TreeNode(3)
        right = TreeNode(6)
        left_left = TreeNode(2)
        left_right = TreeNode(1)
        right_left = TreeNode(5)
        right_right = TreeNode(4)

        self.root = rootNode
        rootNode.left = left
        rootNode.right = right

        left.left = left_left
        left.right = left_right

        right.left = right_left
        right.right = right_right

    def createMinHeap(self):
        rootNode = TreeNode(0)
        left = TreeNode(7)
        right = TreeNode(3)
        left_left = TreeNode(9)
        left_right = TreeNode(8)
        right_left = TreeNode(5)
        right_right = TreeNode(6)

        self.root = rootNode
        rootNode.left = left
        rootNode.right = right

        left.left = left_left
        left.right = left_right

        right.left = right_left
        right.right = right_right
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


# newTree = BinaryTree()
# newTree.insert(5 )
# print(newTree.root.data)
# newTree.insert(7)
# print(newTree.root.data)
# newTree.insert(3)
# print(newTree.root.data)


def Level_Order(node):
    if node is None:
        return

    queue = deque()
    queue.append(node)
    ans_arr = []

    while queue:
        curr_lvl = []
        n = len(queue)
        for i in range(n):
            currNode = queue.popleft()
            curr_lvl.append(currNode.data)

            if currNode.left: queue.append(currNode.left)
            if currNode.right: queue.append(currNode.right)

        ans_arr.append(curr_lvl)

    return ans_arr


def lvl_ord_print(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        currVal = queue.popleft()
        print(currVal.data)
        if currVal.left:
            queue.append(currVal.left)
        if currVal.right:
            queue.append(currVal.right)
    return


def find_max_val_in_binarytree_recursive(root):
    if root is None:
        return float('-inf')

    result = root.data
    left = find_max_val_in_binarytree_recursive(root.left)
    right = find_max_val_in_binarytree_recursive(root.right)
    result = max(result, left, right)
    return result


def find_target_in_treeDFS(root, target):
    if root is None:
        return False

    stack = [root]
    val = []
    while stack:
        current = stack.pop()
        if current.data is target:
            return True

        val.append(current.data)

        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)

    return val


def find_target_in_treeBFS(root, target):
    if root is None:
        return False

    q = deque()
    q.append(root)
    finalVal = []
    while q:
        curr = q.popleft()

        if curr.data is target:
            return True

        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)

        finalVal.append(curr.data)

    return finalVal


def findingTargetRecursively(root, val):
    if root is None: return False
    if root.data is val: return True
    return findingTargetRecursively(root.left, val) or findingTargetRecursively(root.right, val)


def treeSum(root):
    if root is None: return 0

    total = 0
    stack = [root]
    while stack:
        curr = stack.pop()
        total += curr.data

        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)

    return total


def treeSumRecursive(root):
    if root is None: return 0

    return root.data + treeSumRecursive(root.left) + treeSumRecursive(root.right)

def findMin(root):
    if root is None: return

    stack = [root]
    smallest = root.data
    while stack:
        curr = stack.pop()
        smallest = min(curr.data, smallest)

        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)

    return smallest


def findMinRecursive(root):
    if root is None: return float('inf')

    leftVal = findMinRecursive(root.left)
    rightVal = findMinRecursive(root.right)

    return min(root.data, leftVal, rightVal)


def maxPathSumRecursive(root):
    if root is None: return float('-inf')
    if root.left is None and root.right is None:
        return root.data

    maxVal = max(maxPathSumRecursive(root.left), maxPathSumRecursive(root.right))
    return root.data + maxVal

# is there a path that equals this number


def maxPathSum(root):
    if root is None: return 0

    stack = [root]
    currPath = 0
    while stack:
        currVal = stack.pop()

        currPath += currVal.data

        if currVal.left and currVal.right:
            if currVal.left.data > currVal.right.data:
                stack.append(currVal.left)
            else:
                stack.append(currVal.right)

    return currPath


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
