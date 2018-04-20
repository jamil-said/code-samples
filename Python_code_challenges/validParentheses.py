
""" validParentheses
Given a string containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all 
valid but "(]" and "([)]" are not.
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp, opn, clos = ['0'], 0, 0
        for c in s:
            if c == '(' or c == '{' or c == '[': 
                temp.append(c)
                opn += 1
            elif c == ')': 
                if temp[-1] != '(': return False
                temp.pop()
                clos += 1
            elif c == '}': 
                if temp[-1] != '{': return False
                temp.pop()
                clos += 1
            elif c == ']': 
                if temp[-1] != '[': return False
                temp.pop()
                clos += 1
        return opn == clos

print(Solution.isValid(Solution, "[")) # False
print(Solution.isValid(Solution, "([])")) # True



