""" bestTimeBuySellStockII
Say you have an array for which the ith element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (ie, buy one and sell one share of the stock 
multiple times). However, you may not engage in multiple transactions at 
the same time (ie, you must sell the stock before you buy again).
"""


class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            profit += max(0, prices[i+1] - prices[i])     
        return profit


""" Alternative, more complicated, similar speed

class Solution:
    def maxProfit(self, prices):
        temp, res = 0, 0
        for i in range(len(prices)-1):
            if prices[i] <= prices[i+1]:
                temp += (prices[i+1] - prices[i])
            else:
                res += temp
                temp = 0
        return res + temp     
           
"""        

print(Solution().maxProfit([7,1,5,3,6,4])) #7
print(Solution().maxProfit([1,2,3,4,5])) #4
print(Solution().maxProfit([7,6,4,3,1])) #0
