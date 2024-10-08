# this folder will have examples using lambda functions
# map(), filter() and reduce()
from functools import reduce

# MAP
numbers = [1, 2, 3]


def double(a):
  return a * 2


doubleAsLambda = lambda a: a * 2

option1 = map(double, numbers)
option2 = map(doubleAsLambda, numbers)
option3 = map(lambda a: a * 2, numbers)

print(list(option1))
print(list(option2))
print(list(option3))


# FILTER
def isEven(n):
  return n % 2 == 0


opt1 = filter(isEven, numbers)
opt2 = filter(lambda a: a % 2 == 0, numbers)
print(list(opt1))
print(list(opt2))

# REDUCE
expenses = [
  ("New Car", 80000),
  ("New Home", 700000),
  ("Beauty", 5000),
  ("New Wardrobe", 10000),
  ("Mami Gift", 500000),
]


def calculateExpense(total, expenseList):
    total += expenseList[1]
    return total


op1 = reduce(calculateExpense, expenses, 0)
op3 = reduce(lambda a, expense: a + expense[1], expenses, 0)

print(op1)
print(op3)
