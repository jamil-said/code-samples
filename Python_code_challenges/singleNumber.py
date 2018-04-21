
""" singleNumber
Given an array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you 
implement it without using extra memory? 
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        return 2 * sum(set(nums)) - sum(nums)

""" alternative, slower
class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1: return nums[0]
        sortN = sorted(nums)
        if sortN[-1] != sortN[-2]: return sortN[-1]
        for i in range(1, len(nums), 2):
            if sortN[i-1] != sortN[i]: return sortN[i-1]
"""



