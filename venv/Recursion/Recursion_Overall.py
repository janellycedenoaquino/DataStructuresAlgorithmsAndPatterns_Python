"""
recursion:

is created with a stack
calling the function from inside itself over and over again

stack overflow can occur
when you call the stack too many times and have no more space to call it again
"""


def reverse_string(string):
    if len(string) == 0:
        return string

    return reverse_string(string[1:]) + string[0]


def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num-1)


def allPositiveEvenNums(num):
    if num == 2:
        return num

    if num % 2 == 0: print(num)
    return allPositiveEvenNums(num-1)


def fibonacci(idx):
    if idx <= 1:
        return idx

    return fibonacci(idx-1) + fibonacci(idx-2)

