
""" generateParentheses
Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.calcParent(result, '', n, n)
        return result
    
    def calcParent(self, result, current, left, right):
        if left == 0 and right == 0: result.append(current)
        if left > 0: self.calcParent(result, current + '(', left-1, right)
        if left < right: self.calcParent(result, current + ')', left, right-1)


print(Solution().generateParenthesis(3))
"""
[ "((()))", "(()())", "(())()", "()(())", "()()()"]
"""

