
""" maximumSubarray
Find the contiguous subarray within an array (containing at least one 
number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0: return max(nums)
        maxSum, maxSumTmp = float("-inf"), 0
        for i in nums:
            maxSumTmp = max(0, maxSumTmp+i)
            maxSum = max(maxSum, maxSumTmp)
        return maxSum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6

