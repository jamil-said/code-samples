<?php

/* bestTimeBuySellStock
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
*/


class Solution {
    function maxProfit($prices){
        $minPrice = INF;
        $profit = 0;
        foreach($prices as $p) {
            $minPrice = min($minPrice, $p);
            $profit = max($profit, $p - $minPrice);
        }
        return $profit;
    }
}

echo Solution::maxProfit([7, 1, 5, 3, 6, 4]), "\n"; #5
echo Solution::maxProfit([7, 6, 4, 3, 1]), "\n"; #0
echo Solution::maxProfit([3,2,6,5,0,3]), "\n"; #4
echo Solution::maxProfit([1,2]), "\n"; #1
echo Solution::maxProfit([1,2,4]), "\n"; #3
