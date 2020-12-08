
""" pascalsTriangleII
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0] * (rowIndex+1)
        for i in range(rowIndex+1):
            old, result[0] = 1, 1
            for j in range(1, i+1):
                old, result[j] = result[j], old+result[j]
        return result

print(Solution().getRow(3))

