
""" regularExpressionMatching
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p)+1) for i in range(len(s)+1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                if j+1 < len(p) and p[j+1] is '*':
                    dp[i][j] = dp[i][j+2] or match and dp[i+1][j]
                else:
                    dp[i][j] = match and dp[i+1][j+1]
        return dp[0][0]   

print(Solution().isMatch("aa","a")) #False
print(Solution().isMatch("aa","aa")) #True
print(Solution().isMatch("aaa","aa")) #False
print(Solution().isMatch("aa", "a*")) #True
print(Solution().isMatch("aa", ".*")) #True
print(Solution().isMatch("ab", ".*")) #True
print(Solution().isMatch("aab", "c*a*b")) #True
print(Solution().isMatch("ab", ".*c")) #False

