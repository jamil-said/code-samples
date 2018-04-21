
""" removeDuplicatesSortedArray
Given a sorted array, remove the duplicates in-place such that each element 
appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of 
nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    def removeDuplicates(self, nums):
        if len(nums) <= 1: return len(nums)
        prev = 0
        for i in range(1, len(nums)):
            if nums[prev] != nums[i]:
                prev += 1
                nums[prev] = nums[i]
        return prev + 1

print(Solution().removeDuplicates([1, 1, 2]))


