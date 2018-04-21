
""" zigZagConversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a fixed 
font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a 
number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
"""

class Solution:
    def convert(self, s, nRows):
        """
        :type s: str
        :type nRows: int
        :rtype: str
        """ 
        if not s or nRows == 1: return s
        result, step =  '', (2*nRows)-2
        for i in range(nRows):
            for j in range(i, len(s), step):
                result += s[j]
                if 0 < i < nRows-1 and j+step-(2*i) < len(s):
                    result += s[j+step-(2*i)]
        return result


print(Solution().convert("PAYPALISHIRING", 3)) #"PAHNAPLSIIGYIR"

