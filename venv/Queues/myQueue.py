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



