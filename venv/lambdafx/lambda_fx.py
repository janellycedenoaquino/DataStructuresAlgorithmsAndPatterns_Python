# lambda arguments: expression <-- this is the lambda structure
from itertools

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
# sorted
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# sorted_points2D =