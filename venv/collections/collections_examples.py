from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# print("Counter\n")
# # Counter
# val1 = "accceef"
# count = Counter(val1)
# print(count)
# print(count.get("c"))
# print(count.keys())
# print(count.values())
# print(count.items())
# print(list(count.elements()))
# print(count.most_common())  # empty parameter gives the full list ordered
# print(count.most_common(1))  # total most common
# print("_____________________________________\n")
#
# print("namedTuple\n")
#
# # namedtuple
# P = namedtuple('P', 'x,y')
# pt = P(1, 6)
# print(pt.x)
# print(pt.y)
# print(pt)
# print("_____________________________________\n")
#
# print("OrderedDict\n")
# # OrderedDict  --> the update makes the regular dict have this functionality
# val2 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
# print(val2.keys()),
# # print(var2['r']) raises an error
# val2.pop('a')  # pops the last value added in the dictionary
# print("_____________________________________\n")
#
# print("defaultdict\n")
# # defaultdict  -->  same functionality as regular but doesn't raise error
# val3 = defaultdict()  # can not just add values
# val3['a'] = 1
# val3['b'] = 2
# val3['c'] = 3
# print(val3.get("r"))  # if getting a variable that DNE it raises no errors
#
# print("_____________________________________\n")

print("deque\n")
# deque
val4 = deque()
val4.append(1)  # appends at the very end
print("after append(1)  --->", val4)

val4.appendleft(0)  # appends at very beginning
print("after appendleft(0)  --->", val4)

val4.append(3)
val4.append(4)
val4.append(5)
print("after append 3,4,5   --->", val4)

val4.pop()  # deletes last value added
print("after pop()   --->", val4)

val4.popleft()  # deletes first value in queue
print("after popleft()   --->", val4)

val4.extend([1, 2])  # adds list to the end in order passed
print("after extend([1,2])   --->", val4)

val4.extendleft([1, 2])  # adds list to beginning in reverse order
print("after extendleft([1,2])   --->", val4)

val4.rotate(2)  # rotates the queue 2x to the right
print("after rotate(2)   --->", val4)

val4.rotate(-4)  # rotates the queue 4x to the left
print("after rotate(-4 )   --->", val4)

print("_____________________________________\n\n")
