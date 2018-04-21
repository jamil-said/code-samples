
""" longestSubstringNoRepeatingCharacters
Given a string, find the length of the longest substring without repeating 
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the 
answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, left, maxLen = {}, 0, 0
        for i, c in enumerate(s):
            if c in dic and left <= dic[c]: left = dic[c] + 1
            else: maxLen = max(maxLen, i-left+1)
            dic[c] = i
        return maxLen
                
print(Solution().lengthOfLongestSubstring("pwwkew")) #3
print(Solution().lengthOfLongestSubstring("c")) #1
print(Solution().lengthOfLongestSubstring("au")) #2
print(Solution().lengthOfLongestSubstring("dvdf")) #3
print(Solution().lengthOfLongestSubstring("abba")) #2
print(Solution().lengthOfLongestSubstring("tmmzuxt")) #5
