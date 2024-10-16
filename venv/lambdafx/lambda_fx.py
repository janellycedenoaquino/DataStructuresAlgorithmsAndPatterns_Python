# lambda arguments: expression <-- this is the lambda structure
from functools import reduce

# ex:
def addTen(x):
    return x + 10


addTenLambdaForm = lambda x: x + 10


print("addTen regular function answer: ", addTen(10))
print("addTenLambdaForm lambda function answer: ", addTenLambdaForm(10))


# multi line lambda function:

mult = lambda x, y: x * y


def multi(x, y):
    return x * y

print("_____________________________________________\n\n")
print("mult lambda function answer: ", mult(5, 5))
print("multi regular function answer: ", multi(5, 5))

print("_____________________________________________\n\n")


# lamda using sorted map filter and reduce
# sorted(iterable, function)
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
sorted_points2D = sorted(points2D, key=lambda x: x[1])
sorted_points2DSum = sorted(points2D, key=lambda x: x[0]+x[1])
print(points2D)
print(sorted_points2D)  # sorts it by the second index the smallest
print(sorted_points2DSum)  # sorts it by the sum of each


print("_____________________________________________\n\n")
# map(function, iterable)
a = [1, 2, 3, 4, 5, 6, 7]
b = map(lambda x: x*2, a)
print("b = ", list(b))


# list comprehensions
c = [x*2 for x in a]
print("c = ", list(c))


print("_____________________________________________\n\n")
# filter(function, iterable)
d = filter(lambda x: x % 2 == 0, a)
print("d = ", list(d))

# list comprehensions
e = [x for x in a if x %2 == 0]
print("e = ", list(e))



print("_____________________________________________\n\n")
# reduce(function, iterable) combines everything
f = reduce(lambda x, y: x*y, a)
print("f = ", f)

g = ['H', 'e', 'l', 'l', 'o']
h = reduce(lambda x, y: x+y, g)
print("h: ", h)

i = [5, 4, 3, 2, 1]
j = reduce(lambda x, y: x*y, i)
print("j: ", j)