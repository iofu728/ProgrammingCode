# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-10 22:55:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-10 23:01:38

"""
309. Best Time to Buy and Sell Stock with Cooldown Medium
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Accepted 136,858 Submissions 295,554
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if not N:
            return 0
        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(N - 1)]
        for ii in range(1, N):
            dp[ii][0] = max(dp[ii-1][0], dp[ii-1][2] - prices[ii])
            dp[ii][1] = dp[ii-1][0] + prices[ii]
            dp[ii][2] = max(dp[ii-1][2], dp[ii-1][1])
        return max(dp[N-1][1:])
