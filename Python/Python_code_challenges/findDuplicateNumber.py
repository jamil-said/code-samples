"""
 Given an array nums containing n + 1 integers where each integer is 
 between 1 and n (inclusive), prove that at least one duplicate number 
 must exist. Assume that there is only one duplicate number, find the 
 duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be 
    repeated more than once.
"""

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set()
        for i in nums:
            if i in numSet: return i
            else: numSet.add(i)
