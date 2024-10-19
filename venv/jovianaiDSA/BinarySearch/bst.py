""" given a list of random numbers sorted in decreasing order.
find the number asked to find in the fewest steps possible

questions:
    1) what do we return when we find the number? index at which is at
    2) are we always expected to find the number? no
    3) if not there what do we return? -1
    4) as input will we always be receiving numbers?
    5) the fx parms are the list and num to find... anything else? no
    6) negative numbers? yes
    7) how many elements, what is the minimum and the maximum amount? 0-infinity
    8) repeating numbers? yes
    9) you said it was sorted in decreasing order correct? yes


 ex1: [13, 11, 10, 7, 4, 3, 1, 0]
 find: 7
 answer: 3 -- because 7 is at the 3rd position.

 ex2: [3, 1, 0, -7, -14, -23, -41, -50]
 find: -50
 answer: 7 -- because -50 is at the 0th position.

 ex3: [53, 31, 20, 17, 14, 3, 1, 0]
 find: 53
 answer: 0 -- because 53 is at the 0th position.

 edge cases?

brute force:
  start at index 0 and go one by one until you find the given card.


optimized approach:
 if we do binary search we can find the middle and if the number is larger
 or smaller than the number we are searching for we half what we have.
 and repeat until we find the number.


"""
import math


def bruteForceSolution(cards, query):  # this is 0(N)
    position = 0
    steps = 0
    for x in cards:
        steps += 1
        if x == query:
            print("totalsteps: ", steps)
            return position
        position += 1

    print("totalsteps: ", steps)
    return -1


def optimizedApproach(cards, query):  # this is o(nlog(n))
    lo = 0
    hi = len(cards)-1
    steps = 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2  # using // is the same as doing math.floor()
        mid_value = cards[mid]

        if mid_value == query:
            print("total steps: ", steps)
            return mid
        elif mid_value < query:
            hi = mid - 1
            # reason we set hi to mid is to cut the end. not including mid
        elif mid_value > query:
            lo = mid + 1
            # reason we set lo to mid is to cut the beginning. not including mid

    print("total steps: ", steps)
    return -1


print("brute: ", bruteForceSolution(list(range(100000, 0, -1)), 7))
print("__________________________")
print("optimized: ", optimizedApproach(list(range(100000, 0, -1)), 7))
