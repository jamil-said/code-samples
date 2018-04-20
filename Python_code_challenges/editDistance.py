
""" editDistance
Given two words word1 and word2, find the minimum number of steps 
required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lgW1, lgW2 = len(word1), len(word2)
        dp = [i for i in range(lgW2+1)]
        for i in range(1, lgW1+1):
            pre, dp[0] = dp[0], i
            for j in range(1, lgW2+1):
                tmp = dp[j]
                dp[j] = pre if word1[i-1] == word2[j-1] else min(pre, dp[j], dp[j-1]) + 1
                pre = tmp
        return dp[-1]


""" alternative, slower
class Solution:
    def minDistance(self, word1, word2):
        dist = [[i] for i in range(len(word1)+1)]
        dist[0] = [j for j in range(len(word2)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                insert = dist[i][j - 1] + 1
                delete = dist[i - 1][j] + 1
                replace = dist[i - 1][j - 1]
                if word1[i-1] != word2[j-1]:
                    replace += 1
                dist[i].append(min(insert, delete, replace))
        return dist[-1][-1]
"""
