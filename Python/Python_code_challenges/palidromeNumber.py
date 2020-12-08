
""" palidromeNumber
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False #assuming only positives can be palindrome
        return str(x)[::-1] == str(x)
            
print(Solution.isPalindrome(Solution, 121)) #true

