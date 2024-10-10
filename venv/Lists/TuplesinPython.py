tuple1 = (10, 20)
tuple2 = (1, 2, 3, 4, [5, 6], 7)
list1 = [10, 20]


tuple1_set = {tuple1}
# list1-to-set = {list1} <-- this gives an error
# because lists are not immutable and can change at any moment

# tuple2_set = {tuple2} <-- this gives an error because an element
# who happens to be a list is in the tuple and lists are mutable
# tuples are only hashable if the items in the tuple are all hashable

print(f"tuple1: {tuple1[1]} \nlist1:  {list1[1]}")
print(tuple1_set)

