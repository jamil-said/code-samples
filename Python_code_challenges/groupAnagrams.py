
""" groupAnagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.

"""

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for w in strs:
            if ''.join(sorted(w)) in dic: dic[''.join(sorted(w))] += [w]
            else: dic[''.join(sorted(w))] = [w]
        return [v for v in dic.values()]

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["nat","tan"],["bat"],["ate","eat","tea"]]
# or (order doesn't matter): [["tan","nat"],["eat","tea","ate"],["bat"]]
# etc. (many right answers possible)

