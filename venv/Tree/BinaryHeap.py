"""
Binary Heap is a data structure that helps us implement priority queue
operations efficiently. A binary heap is a complete binary tree in which
each node value is >= or <= the values of it's children

ex:                 0                              9
                7       3                      3      6
              9   8   5   6                 2   1   5  4
              Min Heap                        Max Heap


Binary Heaps are complete binary tree:
a binary tree where all levels are completely filled except the last.
also they are filled in a way that the left side is never empty.

ex:                 0                              9
                7       3                      3      6
              9   8   5                         1   5  4
        Complete Binary Tree           Incomplete Binary Tree

Binary Heaps are usually implemented using arrays

"""
from TreeDSA import BinaryTree, TreeNode
from collections import deque

