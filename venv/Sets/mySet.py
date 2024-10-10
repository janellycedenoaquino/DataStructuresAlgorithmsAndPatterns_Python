# Don't feel like doing the class will just play with the methods
# class MySet:
#     set_val = set()
#
#     def __init__(self, elements):
#         for element in elements:
#             self.set_val.add(element)
#
#     def printValues(self):
#         str = ""
#         for elements in self.set_val:
#             str += f"{elements}, "
#         return str
#
#
#     def add_item(self, element):
#         self.set_val.add(element)

set_example = {1, 2, 3, 4}
set_example2 = set({1, 2, 3, 4, 5})
set_example3 = set({0, 7, 8, 9})
print(f"set1: {set_example}")
print(f"set2: {set_example2}")

# set_example.add(7)
# print(set_example)

# print(f"popped element: {set_example.pop()}")  # fifo "first in first out"
# set_example.update({2, 5, 6, 8})  # adds the items provided without repetition
# print(f"updated set_example: {set_example}")

# set_example.remove(5)
# print(f"removed element {set_example}")

# new_set_copy = set_example.copy()
# copy is an independent set and does not point to the address of the old set
# print(new_set_copy)
# new_set_copy.clear()
# print(new_set_copy)
# print(set_example)

print(f"set3: {set_example3}")
# set_example.discard(7)   doesn't throw an error when can't find item to delete
# VS set_example.remove(7)  # does give you an error if you pass item that DNE
print("_______________")
# print(set_example2.difference(set_example))
# print(set_example.union(set_example2))
# print(set_example.intersection(set_example2))
print(set_example.isdisjoint(set_example2))
print(set_example.isdisjoint(set_example3))
print(len(set_example))
