class SLL:
    root = None
    tail = None
    size = 0

    def __init__(self, head_val):
        self.root = ListNode(head_val)
        self.tail = None
        self.size += 1

    def get_size(self):
        return self.size

    def find(self, data):
        currentNode = self.root
        while currentNode is not None:
            if currentNode.data == data:
                return currentNode
            else:
                currentNode = currentNode.next
        return False

    def add(self, data):
        newNode = ListNode(data)
        newNode.next = self.root
        self.root = newNode
        self.size += 1

    def insertAt(self, position, new_node):
        currentNode = self.root
        prev = None

        while currentNode is not None:
            if position == 0:
                prev.next = new_node
                new_node.next = currentNode
                self.size +=1
            prev = currentNode
            currentNode = currentNode.next
            position -= 1

    def append(self, data):
        newNode = ListNode(data)
        currentNode = self.root
        self.size += 1
        while currentNode is not None:
            if currentNode.next is None:
                currentNode.next = newNode
                self.tail = newNode
                break
            else:
                currentNode = currentNode.next

    def get_root(self):
        return self.root

    def removeNodeAtIndex(self, index):  # [92, 0, 33, 1, 5, 7, 24, 53, 45, 77]
        currentNode = self.root
        prev = None
        if index == 0:
            self.root = self.root.next
            self.size -= 1
            return True
        else:
            while currentNode is not None:
                if index == 0:
                    prev.next = currentNode.next
                    self.size -= 1
                    return True
                prev = currentNode
                currentNode = currentNode.next
                index -= 1
        return False

    def remove(self, data):
        currentNode = self.root
        prev = currentNode

        if self.root.data is data:
            self.root = self.root.next
            self.size -= 1
            return True
        else:
            while currentNode is not None:
                if currentNode.data == data:
                    prev.next = currentNode.next
                    self.size -= 1
                    return True
                else:
                    prev = currentNode
                    currentNode = currentNode.next
        return False

    def print_LL(self):
        printedList = []
        currentNode = self.root
        while currentNode is not None:
            printedList.append(currentNode.data)
            currentNode = currentNode.next
        return printedList

    def reverse(self):
        current = self.root
        prev = None
        next = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.root = prev
        return self.root

    def findNthNode(self, position):
        current = self.root
        while current is not None:
            if position == 0:
                return current
            position -= 1
            current = current.next
        return False

    def removeDupes(self):
        LL_set = set()
        current = self.root
        prev = None

        while current is not None:
            if current.data in LL_set:
                prev.next = current.next
                current = current.next
            else:
                LL_set.add(current.data)
                prev = current
                current = current.next
        return False


    def removingDupesFromSortedLL(self):
        curr = self.root
        prev = None

        while curr is not None:
            curr = curr.next

class ListNode:
    data = None
    next = None

    def __init__(self, data, next_val=None):
        self.data = data
        self.next = next_val

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_val):
        self.data = new_val

    def setNext(self, new_val):
        self.next = new_val

newLinkedList = SLL(1)
newLinkedList.append(1)
newLinkedList.append(24)
newLinkedList.append(5)
newLinkedList.append(7)
newLinkedList.append(24)
newLinkedList.append(53)
newLinkedList.append(53)
newLinkedList.append(45)
newLinkedList.append(77)
newLinkedList.add(0)
newLinkedList.add(92)
newLinkedList.add(92)
newLinkedList.add(92)

# newNode = ListNode(33)
# newLinkedList.insertAt(2, newNode)
#
#
# print(newLinkedList.size)
# newLinkedList.remove(77)
# print("removed 92: ", newLinkedList.remove(92))
# print(newLinkedList.print_LL())
# newLinkedList.removeNodeAtIndex(2)
# sorted(newLinkedList.print_LL())
# reversedLLValue = newLinkedList.reverse()
print(newLinkedList.print_LL())


# nthNode = newLinkedList.findNthNode(3)
# print(nthNode.data)
newLinkedList.removeDupes()
print(newLinkedList.print_LL())


