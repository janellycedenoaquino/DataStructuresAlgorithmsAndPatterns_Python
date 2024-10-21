""" remove even elements from list

ex: [3, 2, 4, 7, 10, 6, 5]
return: [3, 7, 5]

approach iterate over list and when find an odd int store it in another list
"""

listEx = [1, 3, 4, 6, 8, 9, 7]
# print(listEx)


def oddIntsOnly(list_val):
    oddList = []
    for x in list_val:
        if (x % 2) != 0:
            oddList.append(x)
    return oddList


# print(oddIntsOnly(listEx))


""" how to reverse a list in place

ex: [1, 2, 3, 4, 5, 6, 7]
return: [7, 6, 5, 4, 3, 2, 1]]

approach: two points one at end one at beginning switch points and return result
"""


def reverseListInPlace(list_val):
    left = 0
    right = len(list_val) - 1

    while left <= right:
        currLeft = list_val[left]
        list_val[left] = list_val[right]
        list_val[right] = currLeft

        left += 1
        right -= 1
    return list_val


# print(reverseListInPlace(listEx))
# this changes the list value in memory because it's changing the list in place


def reverseListNewList(list_val):
    newList = []
    for x in list_val[::-1]:
        print("x from reverseListNewList: ", x)
        newList.append(x)
    return newList


# print(reverseListNewList(listEx))


"""
find minimum value in array

ex: [5, 9, 3, 15, 1, 2]
return: 1

approach: iterate and check minimum so far 

"""


def minvalinlist(list_val):
    return min(list_val)


# print(minvalinlist(listEx))


def minvalinlistSolution(list_val):
    min_val = float("inf")

    for x in list_val:
        min_val = min(x, min_val)
    return min_val


# print(minvalinlistSolution(listEx))


""" return second maximum value 

ex: [1, 3, 4, 6, 8, 9, 7]
return: 8
approach" iterate and keep track of max and second_max return second_max
 
"""


def secondMaxVal(list_val):
    secondMax = len(list_val) - 2
    return sorted(list_val)[secondMax]


print(secondMaxVal(listEx))
print(secondMaxVal([1, 6, 4, 15, 77, 25]))

"""
given a list of ints write a function to move all 0s to end 
while maintaining the relative order of the non zero elements

ex: [0, 1, 0, 4, 12]
return  [1, 4, 12, 0, 0

approach: 
have a left and right checking the value at each side if left is 0 switch
and move to the center until left and right meet 

"""


def moveZerosWithOrder(list_value):
    pointer1 = 0
    pointer2 = 1

    while pointer2 < (len(list_value)):
        if list_value[pointer1] == 0 and list_value[pointer2] != 0:
            # swap
            list_value[pointer1] = list_value[pointer2]
            list_value[pointer2] = 0
            pointer1 += 1
            pointer2 += 1

        elif list_value[pointer1] == 0 and list_value[pointer2] == 0:
            # move pointer2 down
            pointer2 += 1

        else:
            # move pointers down
            pointer1 += 1
            pointer2 += 1

    return list_value


listEx2 = [0, 1, 0, 4, 12, 0, 0, 0]
print(moveZerosWithOrder(listEx2))


def missingNum(list_value):

    list_value.sort()
    prev = list_value[0]

    for x in range(0, len(list_value) + 1):
        if x + 1 != list_value[x]:
            prev = x+1
            break

    return prev


listEx3 = [2, 4, 1, 8, 6, 3, 7]
listEx3 = [2, 4, 1, 8, 6, 5, 3, 7, 9, 11]
print(missingNum(listEx3))


"""
s = "racecar"
return: truth

approach two pointer

"""
def palindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        right -= 1
        left += 1
    return True


print("palindrome: ", palindrome("racecar"))
print("palindrome: ", palindrome("booty"))


