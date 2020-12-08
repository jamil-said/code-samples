
""" validPalindrome
Given a string, determine if it is a palindrome, considering only 
alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question 
to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS = ''
        for c in s:
            if c.isalpha(): newS += c.lower()
            elif c.isdigit(): newS += c
        return newS == newS[::-1]


print(Solution().isPalindrome(".,")) # true
print(Solution().isPalindrome("A man, a plan, a canal: Panama")) # true

