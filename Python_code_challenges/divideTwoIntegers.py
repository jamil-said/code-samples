
""" divideTwoIntegers
Given two integers dividend and divisor, divide two integers without 
using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:

    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store 
    integers within the 32-bit signed integer range: [−231,  231 − 1]. 
    For the purpose of this problem, assume that your function returns 
    231 − 1 when the division result overflows.
"""

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        count, dvdAbs, dvsAbs = 0, abs(dividend), abs(divisor)
        while dvdAbs >= dvsAbs:
            inc = dvsAbs
            i = 0
            while dvdAbs >= inc:
                dvdAbs -= inc
                count += 1 << i
                inc <<= 1
                i += 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            return -(count) if -(count) > -2147483648 else -2147483648
        else:
            return count if count < 2147483647 else 2147483647
           

print(Solution().divide(10, 3)) #3
print(Solution().divide(1, 1)) #1
print(Solution().divide(-1, 1)) #-1
print(Solution().divide(-2147483648, -1)) #2147483647 (careful, max 32 bit numbers)

