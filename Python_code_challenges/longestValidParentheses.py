
""" longestValidParentheses
Given a string containing just the characters '(' and ')', find the 
length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution():
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max(self.calcStr(range(len(s)), -1, {'('}, s), \
                   self.calcStr(reversed(range(len(s))), len(s), {')'}, s))

    def calcStr(self, rg, start, cSet, s):
        count, result = 0, 0
        for i in rg:
            if s[i] in cSet:
                count += 1
            else:
                count -= 1
                if count < 0:
                    start, count = i, 0
                elif count == 0:
                    result = max(result, abs(i-start))
        return result
                

print(Solution().longestValidParentheses("(()")) #2
print(Solution().longestValidParentheses(")()())")) #4
print(Solution().longestValidParentheses("()(()")) #2


