
""" reverseInterger
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers 
within the 32-bit signed integer range. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 0
        if x < 0:
            neg = 1
            x *= -1
        x = int(str(x)[::-1])
        if neg == 1: x *= -1
        if(abs(x) > (2 ** 31 - 1)): return 0
        return x



print(Solution.reverse(Solution, -123)) # -321
print(Solution.reverse(Solution, 1534236469)) # 0 - input is 32-bit output isn't

