"""
A queue is a linear data structure used for storing the data.
it's an ordered list in which insertion are done at one end,
called as rear and deletion are done at the other end as front

The first element inserted is the first one to be deleted.
Hence, it is called as First In First Out (FIFO) list.


"""

import queue


class Queue:
    front = None
    rear = None
    length = 0

    def __init__(self, fist_node):
        self.front = ListNode(fist_node)
        self.rear = self.front
        self.length += 1

    def getLength(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def enqueue(self, element_data):
        newElement = ListNode(element_data)
        if self.isEmpty():
            self.front = newElement
        else:
            self.rear.next = newElement

        self.rear = newElement
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            pop = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
        self.length -= 1
        return pop.data

    def print(self):
        curr = self.front
        arr = []

        while curr is not None:
            arr.append(curr.data)
            curr = curr.next
        return arr

    def first(self):
        return self.front

    def last(self):
        return self.rear


class ListNode:
    data = None
    next = None

    def __init__(self, data_, next_=None):
        self.data = data_
        self.next = next_

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node
        return self.next


def list_of_binary(number):
    list_of_numbers = Queue(bin(1)[2:])

    for i in range(2, number+1):
        list_of_numbers.enqueue(bin(i)[2:])

    return list_of_numbers


# queueVal = list_of_binary(10)
# print(queueVal.print())
# newQueue = Queue(7)
# newQueue.enqueue(8)
# newQueue.enqueue(3)
# newQueue.enqueue(2)
# newQueue.enqueue(4)
# newQueue.enqueue(5)
# print(newQueue.print())
# popped = newQueue.dequeue()
# print("pop: ", popped)
# print("first: ", newQueue.first().data)
# print("last: ", newQueue.last().data)
# print(newQueue.print())


queue1 = queue.Queue()  # when using the extra.Queue() you must use get
queue1.put(1)  # put vs append
queue1.put(7)
queue1.put(9)
# queue1.get()
# print(queue1.qsize())
# queue1.join()
print(queue1.get())  # when using the regular queue you must use popleft()
# print(queue1.full())
# print(queue1.)
print(list(queue1.queue))


def evalRPN(tokens):
    stack = []
    for x in tokens:
        if not stack:
            stack.append(int(x))
        elif x not in '+-/*':
            stack.append(int(x))
        else:
            l = len(stack) - 2
            if x == '+':
                stack[l] = stack[l] + stack.pop()
            elif x == '-':
                stack[l] = stack[l] - stack.pop()
            elif x == '*':
                stack[l] = stack[l] * stack.pop()
            else:
                stack[l] = float(stack[l]) / float(stack.pop())
                stack[l] = int(stack[l])
    return stack[0]

