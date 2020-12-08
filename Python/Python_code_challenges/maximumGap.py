
""" maximumGap
Given an unsorted array, find the maximum difference between the successive 
elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,9,6,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either 3,6 or 6,9 
has the maximum difference 3. 

Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Notes:

    --You may assume all elements in the array are non-negative integers and 
      fit in the 32-bit signed integer range.
    --Try to solve it in linear time/space.
"""

class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxG, numsS = float('-inf'), sorted(set(nums))
        if len(numsS) < 2: return 0
        for i in range(len(numsS)-1):
            tmpG = max(numsS[i:i+2]) - min(numsS[i:i+2])
            maxG = max(maxG, tmpG)
        return maxG


print(Solution().maximumGap([3,9,6,1])) #3
print(Solution().maximumGap([10])) #0

