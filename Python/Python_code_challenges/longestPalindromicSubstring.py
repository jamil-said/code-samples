
""" longestPalindromicSubstring
Given a string s, find the longest palindromic substring in s. You may 
assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        maxI, center, right = 0, 0, 0
        stL = self.addChar(s)
        pal = [0] * len(stL) 
        for i in range(1, len(stL)-1):
            currI = 2 * center - i
            if right > i: pal[i] = min(right-i, pal[currI])
            else: pal[i] = 0
            while stL[i+1+pal[i]] == stL[i-1-pal[i]]:
                pal[i] += 1
            if i+pal[i] > right: center, right = i, i+pal[i]       
        for i in range(1, len(stL)-1):
            if pal[i] > pal[maxI]: maxI = i
        start = (maxI-1-pal[maxI]) // 2
        return s[start:start+pal[maxI]]

    def addChar(self, st):
        stLs = ['<']
        for c in st: 
            stLs.extend([None, c])
        stLs.extend([None, '>'])
        return stLs

print(Solution().longestPalindrome("babad")) # "bab" or "aba"
print(Solution().longestPalindrome("cbbd")) # "bb"
print(Solution().longestPalindrome("abb")) # "bb"


