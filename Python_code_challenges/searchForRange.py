
""" searchForRange
Given an array of integers nums sorted in ascending order, find the 
starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.calcRng(nums, target)
        if start == len(nums) or nums[start] != target: return [-1, -1]
        return [start, self.calcRng(nums, target+1)-1]

    def calcRng(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (right+left)//2
            if nums[mid] < target: left = mid + 1
            else: right = mid
        return left


""" alternative -- not sure about bigO, but this code runtime percentile 
     is 99.63%, same as code above
class Solution:
    def searchRange(self, nums, target):
        try: idx = nums.index(target)
        except ValueError: return [-1, -1]
        return [idx, (len(nums)-1 - nums[::-1].index(target))]
"""

print(Solution().searchRange([5,7,7,8,8,10], 8)) #[3,4]

