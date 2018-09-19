
""" subarrayProductLessThanK
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of 
all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], 
[5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly 
less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        res, start, multi = 0, 0, 1
        for i, num in enumerate(nums):
            multi *= num
            while multi >= k:
                multi //= nums[start]
                start += 1
            res += i-start+1
        return res

print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))#8

