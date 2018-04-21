
""" arrayMaxConsecutiveSum2 -- 30 min
Given an array of integers, find the maximum possible sum you can get 
from one of its contiguous subarrays. The subarray from which this sum 
comes must contain at least 1 element.

Example

For inputArray = [-2, 2, 5, -11, 6], the output should be
arrayMaxConsecutiveSum2(inputArray) = 7.

The contiguous subarray that gives the maximum possible sum is [2, 5], 
with a sum of 7.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The maximum possible sum of a subarray within inputArray.
"""

def arrayMaxConsecutiveSum2(inputArray):
    maxSoFar, maxEndHere = float('-inf'), 0
    for i in inputArray:
        maxEndHere = maxEndHere + i
        if (maxSoFar < maxEndHere): maxSoFar = maxEndHere
        if maxEndHere < 0: maxEndHere = 0  
    return maxSoFar

print(arrayMaxConsecutiveSum2([-2, 2, 5, -11, 6])) # 7
print(arrayMaxConsecutiveSum2([-3, -2, -1, -4])) #-1



