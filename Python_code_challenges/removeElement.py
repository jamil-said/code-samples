
"""removeElement
Given an array and a value, remove all instances of that value in-place 
and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond 
the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of 
nums being 2.
"""

class Solution:
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    def removeElement(self, nums, val):
        i, lastN = 0, len(nums)-1
        while i <= lastN:
            if nums[i] == val:
                nums[i], nums[lastN] = nums[lastN], nums[i]
                lastN -= 1
            else:
                i += 1
        return lastN + 1


print(Solution().removeElement([3,2,2,3], 3)) #2, with nums = [2, 2, ...]
print(Solution().removeElement([], 3)) # 0
print(Solution().removeElement([2], 3)) # 1
print(Solution().removeElement([1], 1)) # 0



