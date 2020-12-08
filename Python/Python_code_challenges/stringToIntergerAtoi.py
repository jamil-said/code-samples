
""" stringToIntergerAtoi
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, 
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no 
given input specs). You are responsible to gather all the input requirements 
up front.

Requirements for atoi:

The function first discards as many whitespace characters as necessary 
until the first non-whitespace character is found. Then, starting from 
this character, takes an optional initial plus or minus sign followed by 
as many numerical digits as possible, and interprets them as a numerical 
value.

The string can contain additional characters after those that form the 
integral number, which are ignored and have no effect on the behavior 
of this function.

If the first sequence of non-whitespace characters in str is not a valid 
integral number, or if no such sequence exists because either str is empty 
or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If 
the correct value is out of the range of representable values, 
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

class Solution:
    def myAtoi(self, st):
        """
        :type st: str
        :rtype: int
        """
        if not st: return 0
        sign, result, tempS = '', '0', self.calcA1(st.lstrip())
        if not tempS: return 0
        tempL = list(tempS)
        if tempL[0] == '-': sign = tempL.pop(0)
        elif tempL[0] == '+': tempL.pop(0)
        if not tempS: return 0
        for i in tempL:
            if i.isdigit(): result += i
            else: break
        result = int(result) if not sign else int(result) * -1
        if result > 2147483647: return 2147483647
        elif result < -2147483648: return -2147483648
        return result

    def calcA1(self, s):
        for i, c in enumerate(s):
            if c == '+' or c == '-' or c.isdigit(): return s[i:]
            elif c.isalpha(): return ''
        return ''


print(Solution().myAtoi("4fd+645jue5648+-")) #4
print(Solution().myAtoi("    efd-645jue5648+-")) #0
print(Solution().myAtoi("+")) #0
print(Solution().myAtoi("abc")) #0
print(Solution().myAtoi(" b11228552307")) #0
print(Solution().myAtoi("       52307e442")) #52307





