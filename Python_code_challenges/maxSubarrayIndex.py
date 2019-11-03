
""" maxSubarrayIndex
Given an array of integers containing at least two integers, find the index 
of the largest increasing sub sequence of integers in the array. If there 
are more than one sequence with the same length, return the first occurring 
one. Return the indexes of the first and last element of the subarray in a 
tuple.

Example:
findSub([10, 3, 7, 9, 0, 15] = (1, 3)
"""

def findSub(arr):
    start, end, curS, curE = 0, 0, -1, -1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            if curS == -1: curS = i-1
            curE = i
        else:
            if curE-curS > end-start: start, end, curS, curE = curS, curE, -1, -1
            else: curS, curE = -1, -1
    if curE-curS > end-start: start, end, curS, curE = curS, curE, -1, -1
    return (start, end)


print(findSub([10, 3, 7, 9, 0, 15])) # (1, 3)
print(findSub([10, 3, -7, -4, 0, 15])) # (2, 5)
print(findSub([4, 3])) # (0, 0)
print(findSub([0, 0, 0, 0, 0])) # (0, 0)
print(findSub([-1, 0, -1, 0, 0])) # (0, 1)
print(findSub([-1, 0, -1, 0, 1])) # (2, 4)

