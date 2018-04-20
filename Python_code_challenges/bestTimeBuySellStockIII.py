
""" bestTimeBuySellStockIII
Say you have an array for which the ith element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete at most 
two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must 
sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prof, prof2, temp, temp2 = 0, 0, float("-inf"), float("-inf")
        for p in prices:
            prof2, temp2 = max(prof2, temp2+p), max(temp2, prof-p)
            prof, temp = max(prof, temp+p), max(temp, -p)
        return prof2

