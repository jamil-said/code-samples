
""" pascalsTriangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Note: on Pascal's Triangle, the extremes are always 1 and the middle is 
composed of the addition of the above two "parents" numbers
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i+1):
                if j in (0, i): result[i].append(1)
                else: result[i].append(result[i-1][j-1] + result[i-1][j])
        return result

