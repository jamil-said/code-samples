
""" secondBiggestInteger
Given an array of unique intergers, return the second biggest integer in it. 
Solve the problem in linear time complexity (O(n)) with constant space (i.e.: 
without copying or creating a new array or similar structure). The array 
is guaranteed to have at least 2 values.

Example: 
secondBig([50, 6, 8, 13, 22, -5, -7, 29]) = 29
"""

def secondBig(arr):
    maxN, maxN2 = float('-inf'), float('-inf')
    for n in arr:
        if n > maxN: maxN2, maxN = maxN, n
        elif n > maxN2: maxN2 = n
    return maxN2

print(secondBig([50, 6, 8, 13, 22, -5, -7, 29])) # 29
print(secondBig([50, 6])) # 6
print(secondBig([6, 50])) # 6
print(secondBig([-5, -7, -9, 29])) # -5
print(secondBig([1, 2, 3, 4])) # 3
print(secondBig([1, 2])) # 1


