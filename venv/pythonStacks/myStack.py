"""
stack is a linear data structure
LIFO data structure


STACK OF PANCAKES -- last one to go on top is the first one you must pick up

stacks is how your program runs for singly threaded programs

Python:
        list
        collection.deque
        queue.LifoQueue

ex:  stk = deque()
     stk.append(5)
     stk.pop()  # returns 89
"""
from collections import deque

stk = deque()
stk.append(5)
stk.append(9)
popped = stk.pop()  # returns 89
print(popped)