
""" longestCommonPrefix
Write a function to find the longest common prefix string amongst an 
array of strings.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        for i in range(len(strs[0])):
            for st in strs[1:]:
                if i >= len(st) or st[i] != strs[0][i]: return strs[0][:i]
        return strs[0]


print(Solution.longestCommonPrefix(Solution, ['hello', 'hero', 
'helloween'])) # 'he'
