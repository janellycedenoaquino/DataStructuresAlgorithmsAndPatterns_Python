from collections import deque

"""
stack_ is a linear data structure
LIFO data structure


stack_ OF PANCAKES -- last one to go on top is the first one you must pick up

stack_s is how your program runs for singly threaded programs

Python:
        list
        collection.deque
        queue.LifoQueue

ex:  stk = deque()
     stk.append(5)
     stk.pop()  # returns 89
"""


class stack_:
  top = None
  next = None
  length = 0

  def __init__(self, node, next=None):
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
    stack_ = []
    topVal = self.top

    while topVal is not None:
      stack_.append(topVal.data)
      topVal = topVal.next

    return stack_


class ListNode:
  data = None
  next = None

  def __init__(self, data, next_val=None):
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
  newstack_ = deque(string.strip())
  charArr = ""

  while newstack_:
    charArr += (newstack_.pop())

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
#     stack_ = deque()
#     iteration = 0
#     print("string: ", string)
#     for c in string:
#         iteration += 1
#         print("\niteration: ", iteration, " start:")
#         if c == '(' or c == '[' or c == '{':
#             stack_.append(c)
#             print("pushed into the stack_: ", c)
#             print("current stack_: ", stack_)
#         else:
#             if not stack_:
#                 return False
#             else:
#                 top = stack_[-1]
#                 print("top: ", top)
#                 if c == ')' and top == '(' \
#                    or c == ']' and top == '[' \
#                    or c == '}' and top == '{':
#                     pop = stack_.pop()
#                     print("c: ", c)
#                     print("popped from stack_: ", pop)
#                     print("current stack_: ", stack_)
#                 else:
#                     return False
#         print("iteration: ", iteration, " end\n\n")
#
#     return not stack_


def isValid(string):
  stack_ = deque()

  for curr_char in string:
    if curr_char == '(' or curr_char == '[' or curr_char == "{":
      stack_.append(curr_char)
    else:
      if not stack_:
        return False
      else:
        topOfstack_ = stack_[-1]
        if curr_char == ')' and topOfstack_ == '(' \
            or curr_char == ']' and topOfstack_ == '[' \
            or curr_char == '}' and topOfstack_ == '{':
          stack_.pop()
        else:
          return False
  return not stack_


# ex1 = "{()}"
# ex2 = "{}(){[{()]}"
# ex3 = "{()"
# ex4 = "{}(){[{()}]}"
# print(isValid(ex1))
# print(isValid(ex2))
# print(isValid(ex3))
# print(isValid(ex4))


def calPoints(operations):
  stack_ = deque()
  total = 0

  for i in operations:
    if i == 'C':
      stack_.pop()
    elif i == 'D':
      prevScore = int(stack_[-1])
      stack_.append(prevScore * 2)
    elif i == '+':
      prev = int(stack_[-1])
      sec_prev = int(stack_[-2])
      stack_.append(prev + sec_prev)
    else:
      stack_.append(int(i))

  # for i in range(len(stack_)):
  #     total += stack_.pop()

  return sum(stack_)


# print(calPoints(["5", "2", "C", "D", "+"]))


def makeGood(s):
  stack_ = deque()

  for letter in s:
    if stack_ and abs(ord(letter) - ord(stack_[-1])) == 32:
      print("calculation made :", letter, " equals: ", ord(letter))
      print("plus inside stack_ value:", stack_[-1], " equals: ", ord(stack__[-1]))
      print("total: the absolute value of ")
      val = stack_.pop()
      print("will pop stack_: ", val)
    else:
      print("pushed '" + letter + "' to stack_")
      stack_.append(letter)

  return "".join(stack_)


# print(makeGood("Pp"))


def dailyTemperatures(temperatures):
  n = len(temperatures)
  answer = [0] * n  # Initialize the result array with 0s
  stack_ = []  # This will store indices of temperatures

  for i in range(n):
    # While stack_ is not empty and the current temperature is greater than the temperature
    # at the index of the stack_'s top element
    while stack_ and temperatures[i] > temperatures[stack_[-1]]:
      idx = stack_.pop()
      answer[idx] = i - idx  # Calculate the number of days waited

    stack_.append(i)  # Add the current index to the stack_

  return answer


def dailyTemperatures2(temperatures):
      answer = [0] * len(temperatures)
      stack_ = []

      for curr_day, curr_temp in enumerate(temperatures):
            while stack_ and temperatures[stack_[-1]] < curr_temp:
              prev_day = stack_.pop()
              answer[prev_day] = curr_day - prev_day

            stack_.append(curr_day)

      return answer


def evalRPN(tokens):
      stack_ = []
      for x in tokens:
        if not stack_:
          stack_.append(int(x))
        elif x not in '+-/*':
          stack_.append(int(x))
        else:
          l = len(stack_) - 2
          if x == '+':
            stack_[l] = stack_[l] + stack_.pop()
          elif x == '-':
            stack_[l] = stack_[l] - stack_.pop()
          elif x == '*':
            stack_[l] = stack_[l] * stack_.pop()
          else:
            stack_[l] = float(stack_[l]) / float(stack_.pop())
            stack_[l] = int(stack_[l])
      return stack_[0]

class Minstack_(object):
  def __init__(self):
    self.stack_ = []
    self.min_stack_ = []
  def push(self, val):
    self.stack_.append(val)
    val = min(val, self.min_stack_[-1] if self.min_stack_ else val)
    self.min_stack_.append(val)

  def pop(self):
    pop = self.stack_.pop()
    self.min_stack_.pop()

    return pop
  def top(self):
    return self.stack_[-1]
  def getMin(self):
    return self.min_stack_[-1]

  def print(self):
    arr = []
    for x in self.stack_:
      arr.append(x)

    return arr



# minstack_ = Minstack_()
# minstack_.push(-2)
# minstack_.push(0)
# minstack_.push(-3)
# print(minstack_.print())
# print(minstack_.getMin())
# print(minstack_.pop())
# print(minstack_.print())
# print(minstack_.getMin())
# print(minstack_.top())
# Your Minstack_ object will be instantiated and called as such:
# obj = Minstack_()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
given a list of temperatures respond with a formulated list of how many days 
to get warmer per temperature.

example: 
given these temperatures : [73, 74, 75, 71, 69, 72, 76, 73]
return this              : [1,   1,  4,  2,  1,  1,  0,  0]

because 73 the next day is 74 so it takes one day to get warmer
for 75 it takes 4 days because the warmest after 75 is 76 which happens in 4 days


the reason we want to use a stack_ is because we have an unsorted list
which has to be evaluated by checking the one further up front
and we have to  calculate some difference between the points

anything we need to look back at a previous number

"""
def dailyTemperatures(temperatures):
        stack_ = []
        finalArr = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
          while stack_ and temp > stack_[-1][1]:
            i, t = stack_.pop()
            finalArr[i] = idx - i

          stack_.append([idx, temp])
        return finalArr


value = dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])


# print(value)


"""
evaluate reverse polish notation

ex: ["2", "1", "+", "3", "*"]
answer: 9
why: 2+1 = 3 *3 = 9

2 into stack_ 1 into stack_ 
we found an operator do what we do this case 2+1 store value into answer
find 3 add to stack_ 
find another operator times the numbers we have in answer add it to stack_
return the value we have after loop ends
if we have anything left in stack_ add it to the value we have 



"""

def evalRN(tokens):
  stack_ = []

  for i in tokens:
    if i in '-+/*':
      y = stack_.pop()
      x = stack_.pop()
      if i == '-':
        ans = x - y
      elif i == '+':
        ans = x + y
      elif i == '*':
        ans = x * y
      elif i == '/':
        # if x == 0 or y == 0:
        #   ans = 0
        # else:
          ans = int(float(x / y))
      stack_.append(ans)
    else:
      stack_.append(int(i))
  return stack_[0]


# print(evalRN(["2","1","+","3","*"]))
# print(evalRN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

"""
basic calculator should evaluate a mathematical expression 
the same way polish notation evaluates mathematical expressions 
but the way it does it it's the regular way. where you have an equation like
ex:
input:  "(8 + 100) + (13 - 8 - (2+1))"
output: 110

you have to account for spaces numbers and parenthesis
 
 approach: use a stack_ add numbers to the stack_
 when you encounter a "+-*/" you know you have to do an operation with the 
 number following it 
 when encounter a "(" you have to evaluate what is inside of it until you 
 encounter a ")"
 
iterate through the string ex: "(8 + 100) + (13 - 8 - (2+1))"

* first thing we find is a "("  we store the result we have previously calc in 
a stack_ so that when we are ready to use it we can pop and use. in this first
case it doesn't do anything because the result is 0

* then we find the number 8 we take that number and since the number is a str
we don't know if the next value is a digit we need to store this in a variable 
until we know we have to full number.
for example the number: "123" in string form 
  we find 1 first we store it
  then we find 2 and to be able to store this we need to append it or
  do some calculation. which could look like number = number * 10 + int(i)
  this works because in the first iteration we find 1 so number is 0 
  so 0 * 10(tenth place) is 0 + int(i) integer found ==  1
  then we find 2: in this iteration number is 1 from the prev calculation
  number = number * 10 + int(i) or 1 * 10 + 2 
  timing it by 10 adds a digit to our number without damaging the value
  then adding the number found makes it the number we need
  lastly we add 3 so this iteration will look like number = 12 * 10 + 3
  12 * 10 == 120 <-- we added a digit to out prev amount. + 3 and appended the num
  
  another way to do it is by having number as a string and appending every number 
  found then when we need it converting it to an int -- try this
 
* then we find an space which we skip

* then we find a "+" this makes us know whatever the next number is is either
supposed to be positive or be added to what we previously have in the stack_
so we can store this sign in a variable to use later 
we want to update our result to be  whatever value we have in number * the sign
we have stored before changing the sign to the new one we found
then we want to assign the new value to sign and reset our current
we want to also reset our current number to zero after we store it in the stack_

* then we find another space which we will do the same as before
then we find a number 1 we calculate it's place


"""
# def basicCalc(s):
#     stack_ = []
#     currNum = 0
#     sign = 1
#     result = 0
#
#     for i in s:
#       if i.isdigit():
#         currNum = currNum * 10 + int(i)
#       elif i in '+-':
#         result += (currNum*sign)
#         currNum = 0
#         sign = -1 if sign == '-' else 1
#       elif i == '(':
#         stack_.append(result)
#         stack_.append(sign)
#         result = 0
#         sign = 1
#       elif i == ')':
#         result += (currNum*sign)
#         result *= stack_.pop()
#         result += stack_.pop()
#         currNum = 0
#
#
#     return result + (currNum*sign)
#
#
#
# print(basicCalc("(8 + 100) + (13 - 8 - (2+1))"))
# print(eval("(8 + 100) + (13 - 8 - (2+1))"))


"""
remove adjacent strs 
ex: 
input:  "abcddeea"
output: "abca"
reason: there are no more alike letters next to one another

ex2:
input:  "abbaccdeedaa"
output: ""
reason: all alike letters are next to one another

use a stack_ to store the last value found check next value and compare to new
if same pop is not append keep checking and popping

"""


def rem_adj_str(s):
    stack_ = []

    for i in s:
        if stack_ and stack_[-1] == i:
            stack_.pop()
        else:
            stack_.append(i)

    return ''.join(stack_)


print(rem_adj_str("abcddeea"))
print(rem_adj_str("abbaccdeedaa"))


"""
minimum remove to make valid parentheses

ex: 
input: “(((abc)(to)((q)()(”
output: “(abc)(to)(q)()”

ex2: 
input:  “)((ab)c))(ac(op)t(())(”
output: “((ab)c)ac(op)t(())”


approach: iterate through the string 
append the values found into a new string 
when we find an opening parenthesis
we add to stack_ 
we keep going and store it and if find a closing 
we only add it if we have a matching opening in the stack_ 

"""


def min_remove_parentheses(s):
    stack_ = []
    final_string = [''] * len(s)

    for idx, i in enumerate(s):
        if i == '(':
            stack_.append([idx, i])
            final_string.append("")
        elif i == ')':
            if stack_:
                pop_idx, pop_i = stack_.pop()
                final_string[pop_idx] = pop_i
                final_string[idx] = i
        else:
            final_string[idx] = i

    return ''.join(final_string)


# print("input:  (((abc)(to)((q)()(")
# print("output: (abc)(to)(q)()")
# print('answer:', min_remove_parentheses("(((abc)(to)((q)()("))
# print("\n_______________________________\n")
# print("input:  )((ab)c))(ac(op)t(())(")
# print("output: ((ab)c)ac(op)t(())")
# print('answer:', min_remove_parentheses(")((ab)c))(ac(op)t(())("))


def is_valid(s):
  stack_ = []

  for i in s:
    if i in '([{':
      stack_.append(i)
    elif i in ')]}':
      if stack_:
        if stack_[-1] == '(' and i == ')':
          stack_.pop()
        elif stack_[-1] == '[' and i == ']':
          stack_.pop()
        elif stack_[-1] == '{' and i == '}':
          stack_.pop()
        else:
          return False
      else:
        return False


  # Replace this placeholder return statement with your code
  return len(stack_) == 0



print("input:  “(){}[]”")
print("output: True")
print('answer:', is_valid("(){}[]"))
print("\n_______________________________\n")
print("input:  {}[]{}[{}])")
print("output: False")
print('answer:', is_valid("{}[]{}[{}])"))



x1 = ["2","1","+","3","*"]
Output =  9

x2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
"""
["2","1","+","3","*"]
Output: 9


"""
def polishNo(arr):
    stack = []

    for x in arr:
        if x in '-+/*':
            val2 = stack.pop()
            val1 = stack.pop()

            if x == '-':
                ans = (val2 - val2)
            elif x == '*':
                ans = (val1 * val2)
            elif x == '/':
                ans = int(float(val1 / val2))
            else:
                ans = (val1 + val2)
            stack.append(ans)
        else:
            stack.append(int(x))

    return stack[0]

print("plishnoanswer: ",polishNo(x1))
print("plishnoanswer: ",polishNo(x2))