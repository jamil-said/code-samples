
""" matrixToSortedArray
Create an efficient function that accepts a matrix where every number is 
greater or equal to the numbers on its right and bottom, and outputs a 
sorted array 
"""

#brute force, actually faster than many alternatives:
def matrixToSortedArray(mtx):
    if not mtx: return []
    result = []
    for row in mtx:
        result.extend(row)
    return sorted(result)


print(matrixToSortedArray([[1, 4, 7, 11, 15],
                            [2, 5, 8, 12, 19],
                            [3, 6, 9, 16, 22],
                            [10, 13, 14, 17, 24],
                            [18, 21, 23, 26, 30]]))
print(matrixToSortedArray([[1, 3, 7, 11, 15],
                            [2, 5, 8, 12, 19],
                            [3, 6, 9, 16, 22],
                            [10, 13, 14, 17, 24]]))                            
print(matrixToSortedArray([]))


