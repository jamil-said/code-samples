
""" diagonalTraverse
Given a matrix of M x N elements (M rows, N columns), return all elements 
of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
You must traverse the diagonals in "zigzag", starting on the first element 
and going up, and then traverse the next diagonal going down, and then 
later going up again, etc.

Note:

    The total number of elements of the given matrix will not exceed 10,000.
"""

class Solution:
    def findDiagonalOrder(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: List[int]
        """
        if not arr or not arr[0]: return []
        result, row, col, fIdx = [], 0, 0, 0
        factor = [[-1, 1], [1, -1]]
        for i in range(len(arr)*len(arr[0])):
            result.append(arr[row][col])
            row += factor[fIdx][0]
            col += factor[fIdx][1]
            if row >= len(arr):
                row = len(arr) - 1
                col += 2
                fIdx = 1 - fIdx
            elif col >= len(arr[0]):
                col = len(arr[0]) - 1
                row += 2
                fIdx = 1 - fIdx
            elif row < 0:
                row = 0
                fIdx = 1 - fIdx
            elif col < 0:
                col = 0
                fIdx = 1 - fIdx  
        return result

print(Solution().findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])) # [1,2,4,7,5,3,6,8,9]

