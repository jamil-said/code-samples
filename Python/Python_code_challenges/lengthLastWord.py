
""" lengthLastWord
Given a string s consists of upper/lower-case alphabets and empty space 
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space 
characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or not any(c.isalpha() for c in s): return 0
        return len(s.split()[-1])

print(Solution().lengthOfLastWord("Hello World")) #5

