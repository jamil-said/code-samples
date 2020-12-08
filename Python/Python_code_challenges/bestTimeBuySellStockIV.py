
""" bestTimeBuySellStockIV
Say you have an array for which the ith element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete at most 
k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must 
sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices)//2: return self.maxNProf(prices)
        return self.maxKProf(prices, k)

    def maxNProf(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            profit += max(0, prices[i+1] - prices[i])     
        return profit

    def maxKProf(self, prices, k):
        maxBuy = [float("-inf") for i in range(k+1)]
        maxSell = [0 for i in range(k+1)]
        for i in range(len(prices)):
            for j in range(1, min(k, i//2+1)+1):
                maxBuy[j] = max(maxBuy[j], maxSell[j-1] - prices[i])
                maxSell[j] = max(maxSell[j], maxBuy[j] + prices[i])
        return maxSell[k]


