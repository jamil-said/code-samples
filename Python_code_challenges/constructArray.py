
""" 10 min -- constructArray
Given an integer size, return an array containing each integer from 1 to 
size in the following order:

1, size, 2, size - 1, 3, size - 2, 4, ...

Example

For size = 7, the output should be
constructArray(size) = [1, 7, 2, 6, 3, 5, 4].

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer size

A positive integer.

Guaranteed constraints:
1 ≤ size ≤ 15.

[output] array.integer
"""

def constructArray(size):
    result = []
    for i in range(size):
        result.append(i+1)
        if len(result) == size: return result
        result.append(size-i)
        if len(result) == size: return result
        
print(constructArray(7)) # [1, 7, 2, 6, 3, 5, 4]
