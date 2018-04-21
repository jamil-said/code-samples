
""" deleteOperationTwoStrings
Given two words word1 and word2, find the minimum number of steps required 
to make word1 and word2 the same, where in each step you can delete one 
character in either string.

Example 1:

Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to 
make "eat" to "ea".

Note:

    The length of given words won't exceed 500.
    Characters in given words can only be lower-case letters.
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lenW1, lenW2 = len(word1), len(word2)
        prev = [i for i in range(lenW2+1)]
        for i in range(lenW1):
            dp = [i+1]
            for j in range(lenW2):
                if word1[i] == word2[j]:
                    dp.append(prev[j])
                else:
                    dp.append(min(prev[j+1], dp[-1]) + 1)
            prev = dp
        return prev[-1]


""" alternative, slower
class Solution:
    def minDistance(self, word1, word2):
        lenW1, lenW2 = len(word1), len(word2)
        dp = [[0] * (lenW2+1) for i in range(2)]
        for i in range(lenW1):
            for j in range(lenW2):
                dp[(i+1)%2][j+1] = max(dp[i%2][j+1], dp[(i+1)%2][j], \
                                       dp[i%2][j] + (word1[i] == word2[j]))
        return lenW1 + lenW2 - 2*dp[lenW1%2][lenW2]
"""



