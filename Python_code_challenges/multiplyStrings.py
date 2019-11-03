
""" multiplyStrings

Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 
    0 itself.
    You must not use any built-in BigInteger library or convert the inputs 
    to integer directly.

"""

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        int1, int2 = 0, 0
        for c in num1:
            int1 *= 10
            int1 += int(c)
        for c in num2:
            int2 *= 10
            int2 += int(c)
        return str(int1 * int2)


print(Solution().multiply('2', '3')) #6

