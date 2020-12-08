
""" combinationSum2
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution:
    def combinationSum2(self, arr, targ):
        """
        :type arr: List[int]
        :type targ: int
        :rtype: List[List[int]]
        """
        results = []
        Solution.calcComb(self, sorted(arr), targ, 0, [], results)
        if len(results) == 0: return []
        return results
        
    def calcComb(self, nums, targ, idx, path, results):
        if targ == 0:
            if path not in results: results.append(path)
            return 
        for i in range(idx, len(nums)):
            if nums[i] > targ or targ-nums[i] < 0: return
            Solution.calcComb(self, nums, targ-nums[i], i+1, path+[nums[i]], results)


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
# [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]] or in orther order such as
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

