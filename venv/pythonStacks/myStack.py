from collections import deque

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


class Stack:
    top = None
    next = None
    length = 0

    def __init__(self, node, next = None):
        self.top = node
        self.next = next
        self.length += 1

    def getLength(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def pop(self):
        popVal = self.top.data
        self.top = self.top.next
        self.length -= 1
        return popVal

    def push(self, new_val):
        temp = new_val
        temp.next = self.top
        self.top = temp
        self.length += 1

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data

    def print(self):
        stack = []
        topVal = self.top

        while topVal is not None:
            stack.append(topVal.data)
            topVal = topVal.next

        return stack


class ListNode:
    data = None
    next = None

    def __init__(self, data, next_val = None):
        self.data = data
        self.next = next_val

    def getData(self):
        return self.data

    def setData(self, new_val):
        self.data = new_val

    def getNext(self):
        return self.next

    def setNext(self, new_val):
        self.next = new_val



"""
Runlength encoding
ex: "aaaabbccc"
answer: 4a2b3c


ex: "aaaabbccc1a"
answer: 4a2b3c1a


approach 
    create a counter and two pointers 
    once the pointers are not the same val calulate and restart count
    
"""


def run_length_encoding(string_val):
    answer = []
    counter = 1
    pointer1 = 0
    pointer2 = 1

    while pointer1 is not None:
        if string_val[pointer1] == string_val[pointer2]:
            counter += 1
            pointer2 += 1
            if pointer2 >= len(string_val):
                answer.append(str(counter) + string_val[pointer1])
                return answer
        else:
            answer.append(str(counter) + string_val[pointer1])
            pointer1 = pointer2
            pointer2 += 1
            counter = 1
            if pointer2 >= len(string_val):
                answer.append(str(1) + string_val[pointer1])
                return answer


def reverseSTR(string):
    newStack = deque(string.strip())
    charArr = ""

    while newStack:
        charArr += (newStack.pop())

    return charArr


"""
Given an array of ints. for each element in the array, find its next
greater element in that array. the next greater element is the first element
towards right, which is greater than the current element.

example --

input:  [4, 7, 3, 4, 8, 1]
Output: [7, 8, 4, 8, -1, -1]


two pointers is the obvious 
"""


def greatest_element_2points(arr):
    current = 0
    right = 1
    finalArr = []

    while current < len(arr):
        if right >= (len(arr) - 1):
            current += 1
            right = current + 1
            finalArr.append(-1)
        elif arr[current] < arr[right]:
            finalArr.append(arr[right])
            current += 1
            right = current + 1
            if current >= len(arr) - 1:
                finalArr.append(-1)
                return
        else:
            right += 1

    return finalArr


"""
Given a string s, containing just the characters '(', ')', '[', ']', '{', '}'
determine if the input string is valid. An input string is valid if:
- open brackets must be closed by the same type of bracket
- open brackets must be closed in correct order.

ex:     
    input: str = "{()}" output: true
    input: str = "{]"   output: false
    input: str = "{()"  output: false
    
approach: 
    "{()}"
     |  |
     
     "{()[()]}"
       |   |
     
"""


# def isValid(string):
#     stack = deque()
#     iteration = 0
#     print("string: ", string)
#     for c in string:
#         iteration += 1
#         print("\niteration: ", iteration, " start:")
#         if c == '(' or c == '[' or c == '{':
#             stack.append(c)
#             print("pushed into the stack: ", c)
#             print("current stack: ", stack)
#         else:
#             if not stack:
#                 return False
#             else:
#                 top = stack[-1]
#                 print("top: ", top)
#                 if c == ')' and top == '(' \
#                    or c == ']' and top == '[' \
#                    or c == '}' and top == '{':
#                     pop = stack.pop()
#                     print("c: ", c)
#                     print("popped from stack: ", pop)
#                     print("current stack: ", stack)
#                 else:
#                     return False
#         print("iteration: ", iteration, " end\n\n")
#
#     return not stack


def isValid(string):
    stack = deque()

    for curr_char in string:
        if curr_char == '(' or curr_char == '[' or curr_char == "{":
            stack.append(curr_char)
        else:
            if not stack:
                return False
            else:
                topOfStack = stack[-1]
                if curr_char == ')' and topOfStack == '(' \
                    or curr_char == ']' and topOfStack == '[' \
                    or curr_char == '}' and topOfStack == '{':
                    stack.pop()
                else:
                    return False
    return not stack


ex1 = "{()}"
ex2 = "{}(){[{()]}"
ex3 = "{()"
ex4 = "{}(){[{()}]}"
print(isValid(ex1))
print(isValid(ex2))
print(isValid(ex3))
print(isValid(ex4))


def calPoints( operations):
    stack = deque()
    total = 0

    for i in operations:
        if i == 'C':
            stack.pop()
        elif i == 'D':
            prevScore = int(stack[-1])
            stack.append(prevScore*2)
        elif i == '+':
            prev = int(stack[-1])
            sec_prev = int(stack[-2])
            stack.append(prev + sec_prev)
        else:
            stack.append(int(i))

    # for i in range(len(stack)):
    #     total += stack.pop()

    return sum(stack)


print(calPoints(["5", "2", "C", "D", "+"]))


def makeGood(s):
    stack = deque()

    for letter in s:
        if stack and abs(ord(letter) - ord(stack[-1])) == 32:
            print("calculation made :", letter, " equals: ", ord(letter) )
            print("plus inside stack value:", stack[-1], " equals: ", ord(stack[-1]))
            print("total: the absolute value of ")
            val = stack.pop()
            print("will pop stack: ", val)
        else:
            print("pushed '" + letter + "' to stack")
            stack.append(letter)

    return "".join(stack)


print(makeGood("Pp"))