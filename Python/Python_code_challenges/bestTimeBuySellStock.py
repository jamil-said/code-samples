""" bestTimeBuySellStock
Say you have an array for which the ith element is the price of a given 
stock on day i.

If you were only permitted to complete at most one transaction (ie, buy 
one and sell one share of the stock), design an algorithm to find the 
maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be 
larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    def maxProfit(self, prices):
        maxProf, minPrice = 0, float("inf")
        for p in prices:
            minPrice = min(minPrice, p)
            maxProf = max(maxProf, p-minPrice)  
        return maxProf


"""Alternative: much slower and more complicated, this is a slightly enhanced "brute force" version

class Solution:
    def maxProfit(self, prices):
        res, tmp = 0, 0
        for i in range(len(prices)-1):
            if (prices[i+1] > prices[i]):
                for j in range(len(prices)):
                    if (j > i) and (prices[j] > res):
                        tmp = prices[j] - prices[i]
                        res = max(res, tmp)
        return res

"""        


print(Solution().maxProfit([7, 1, 5, 3, 6, 4])) #5
print(Solution().maxProfit([7, 6, 4, 3, 1])) #0
print(Solution().maxProfit([3,2,6,5,0,3])) #4
print(Solution().maxProfit([1,2])) #1
print(Solution().maxProfit([1,2,4])) #3
