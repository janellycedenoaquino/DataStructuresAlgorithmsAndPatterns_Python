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

        if position == 0:
            new_node.next = self.root
            self.root = new_node
            return True
        while currentNode is not None:
            if position == 0:
                prev.next = new_node
                new_node.next = currentNode
                self.size += 1
                return True
            prev = currentNode
            currentNode = currentNode.next
            position -= 1
        if prev is not None:
            prev.next = new_node
        return False

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
        while curr is not None and curr.next is not None:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next

    def insertNodeInSLL(self, node):
        curr = self.root.next
        prev = self.root
        while curr is not None:
            if curr.data >= node.data:
                prev.next = node
                node.next = curr
                return True
            else:
                prev = curr
                curr = curr.next

    def loop(self):
        curr = self.root
        prev = self.root

        while curr is not None:
            prev = prev.next
            curr = curr.next.next
            if curr is prev:
                return True
        return False

    def print_loop(self):
        loop = []
        slow = self.root
        fast = self.root

        while fast is not None and fast.next is not None:
            loop.append(slow.data)
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return loop

        return loop

    def startOfLoopSll(self):
        slow = self.root
        fast = self.root

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                print("before it was: ", slow.data)
                return self.getStartingNode(slow).data

        return False

    def getStartingNode(self, slow):
        temp = self.root
        while slow != temp:
            temp = temp.next
            slow = slow.next
        return temp


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


newLL = SLL(0)
newLL.append(1)
newLL.append(3)
newestNode = ListNode(7)
firstNode = ListNode(2)
newLL.insertAt(2, firstNode)
newLL.append(8)
newLL.append(9)
newLL.append(4)

newLL.insertAt(3, newestNode)
newestNode.next = firstNode



# print(newLL.loop())
# print(newLL.print_LL())
print(newLL.print_loop())  # [2, 0, 1, 3, 8, 9, 4, 7]
print(newLL.startOfLoopSll())
# print(newLL.print_LL())

