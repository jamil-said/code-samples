
""" rotateArray
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated 
to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different 
ways to solve this problem.

Related problem: Reverse Words in a String II
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, count = 0, 0
        while count < len(nums):
            curr = start
            prev = nums[curr]
            while True:
                idx = (curr + k) % len(nums)
                nums[idx], prev = prev, nums[idx]
                curr = idx
                count += 1
                if start == curr: break
            start += 1



