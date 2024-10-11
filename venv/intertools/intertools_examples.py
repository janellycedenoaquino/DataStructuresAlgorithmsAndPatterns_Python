from itertools import product, permutations, combinations, accumulate, groupby, \
  combinations_with_replacement, \
  count, cycle, repeat  # <-- infinite iterators
import operator

# product
print("product:\n")
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))
print("________________________")
print("________________________\n")

# permutations
print("permutations:\n")
a = [1, 2, 3]
perm = permutations(a)  # of all items
perm2 = permutations(a, 2)  # of two items
perm3 = permutations(a, 4)  # of 4 items
print(list(perm))
print(list(perm2))
print(list(perm3))  # empty because there are not 4 items
print("________________________")
print("________________________\n")

# combinations
print("combinations:\n")
a = [1, 2, 3, 4]
comb = combinations(a, 2)  # must pass the length of combinations
comb2 = combinations_with_replacement(a, 2)
print(list(comb))  # does not show repeating combinations
print(list(comb2))  # to show repeating numbers
print("________________________")
print("________________________\n")

# accumulate
print("accumulate:\n")
a = [1, 2, 3, 4]
acc = accumulate(a)  # adds last element to next and so on
mult = accumulate(a, func=operator.mul)  # multiplies prev element to next
div = accumulate(a, func=operator.truediv)  # divides prev element to next
print(a)
print(list(acc))
print(list(mult))
print(list(div))
print("________________________")
print("________________________\n")


# groupby

def smaller_than_3(x):
    return x < 3


obj = [{"name": "jay", "age": 29},
       {"name": "cleon", "age": 27},
       {"name": "yairy", "age": 20},
       {"name": "yane", "age": 30},
       {"name": "jari", "age": 24},
       {"name": "noemi", "age": 24}]

print("groupby:\n")
a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)  # groups < 3 and groups > 3
group_obj2 = groupby(a, key=lambda x: x < 3)
group_obj3 = groupby(obj, key=lambda x: x["age"] < 25)

for key, value in group_obj:
    print(key, list(value))

print("________________________\n lambda:")
for key, value in group_obj2:
    print(key, list(value))

for key, value in group_obj3:
    print(key, list(value))

print("________________________")
print("________________________\n")


# count
print("count:\n")
# makes an infinite loop that starts at given value
for i in count(7):
  if i > 10:
    break
  print(i)

print("________________________")
print("________________________\n")


# cycle
print("cycle:\n")
a = [1, 2, 3, 4, 5, 6, 7]
breakVar = 20
# cycles an infinite loop that starts at given value

for i in cycle(a):
    if breakVar == 0:
        break
    print(i)
    breakVar -= 1


print("________________________")
print("________________________\n")


# repeat
print("repeat:\n")
a = [1, 2, 3, 4, 5, 6, 7]
# cycles an infinite loop that starts at given value

for i in repeat(a, 7):  # second value is how many times it will repeat
    print(i)

for i in repeat(1, 7):  # second value is how many times it will repeat
    print(i)


print("________________________")
print("________________________\n")

