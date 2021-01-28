""" arrayMaxConsecutiveSum
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

    2 + 3 = 5;
    3 + 5 = 8;
    5 + 1 = 6;
    1 + 6 = 7.
    Thus, the answer is 8.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer inputArray

    Array of positive integers.

    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 105,
    1 ≤ inputArray[i] ≤ 1000.

    [input] integer k

    An integer (not greater than the length of inputArray).

    Guaranteed constraints:
    1 ≤ k ≤ inputArray.length.

    [output] integer

    The maximal possible sum.
"""


def arrayMaxConsecutiveSum(a, k):
    res, temp = sum(a[:k]), sum(a[:k])
    for i in range(k, len(a)):
        temp = temp - a[i-k] + a[i]
        res = max(res, temp)
    return res
    

print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2)) # 8
print(arrayMaxConsecutiveSum([963, 741, 22, 851, 399, 382, 190, 247, 494, 452, 891, 
532, 795, 920, 465, 831, 344, 391, 582, 897, 763, 951, 735, 806, 320, 702, 200, 59, 
870, 345, 695, 321, 817, 83, 416, 36, 914, 335, 117, 985, 690, 303, 875, 556, 292, 
309, 496, 791, 509, 360, 235, 784, 607, 341], 23)) # 14232
