<?php

/* bestTimeBuySellStockII
Say you have an array for which the ith element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (ie, buy one and sell one share of the stock 
multiple times). However, you may not engage in multiple transactions at 
the same time (ie, you must sell the stock before you buy again).
*/


class Solution {
    function maxProfit($prices) {
        $profit = 0;
        if(count($prices) === 1)
            return 0;
        foreach(range(0, count($prices)-2) as $i) {
            $profit += max(0, $prices[$i+1]-$prices[$i]);
        }
        return $profit;
    }
}  


echo Solution::maxProfit([7,1,5,3,6,4]), "\n"; #7
echo Solution::maxProfit([1,2,3,4,5]), "\n"; #4
echo Solution::maxProfit([7,6,4,3,1]), "\n"; #0
echo Solution::maxProfit([1]), "\n"; #0
