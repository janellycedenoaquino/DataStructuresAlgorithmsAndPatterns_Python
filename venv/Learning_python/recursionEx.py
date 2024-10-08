# factorial example using recursion

def factorialOf(num):
    if num == 1: return 1
    return num * factorialOf(num - 1)


factorialOfThree = factorialOf(3)
factorialOfFour = factorialOf(4)
factorialOfFive = factorialOf(5)

print(f"""
  factorial of 3: {factorialOfThree}
  factorial of 4: {factorialOfFour}
  factorial of 5: {factorialOfFive}""")
