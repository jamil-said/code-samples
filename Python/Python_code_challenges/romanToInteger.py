
""" romanToInteger
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def romanToInt(self, s):
        dicNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, \
        "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            if i > 0 and dicNum[s[i]] > dicNum[s[i - 1]]:
                num += dicNum[s[i]] - 2 * dicNum[s[i - 1]]
            else:
                num += dicNum[s[i]]
        return num

print(Solution.romanToInt(Solution, "DCXXI")) #621


