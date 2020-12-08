
""" ImplementStr
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 
if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle) 

print(Solution().strStr("hello", "ll")) # 2


