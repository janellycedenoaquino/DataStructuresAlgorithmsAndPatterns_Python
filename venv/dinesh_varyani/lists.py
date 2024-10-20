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

