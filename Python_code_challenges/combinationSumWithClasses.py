
""" combinationSum (using classes)
Given a set of candidate numbers (candidates) (without duplicates) and a 
target number (target), find all unique combinations in candidates where 
the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number 
of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:
    def combinationSum(self, arr, targ):
        """
        :type arr: List[int]
        :type targ: int
        :rtype: List[List[int]]
        """
        results = []
        arr.sort()
        Solution.calcComb(self, arr, targ, 0, [], results)
        if len(results) == 0: return []
        return results
        
    def calcComb(self, nums, targ, idx, path, results):
        if targ < 0: return
        if targ == 0:
            results.append(path)
            return 
        for i in range(idx, len(nums)):
            if nums[i] > targ: break
            Solution.calcComb(self, nums, targ-nums[i], i, path+[nums[i]], results)


print(Solution().combinationSum([2,3,5], 8))
"""
[[2,2,2,2],
  [2,3,3],
  [3,5]]
"""

