# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-23 19:48:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-23 19:49:08

"""
714. Best Time to Buy and Sell Stock with Transaction Fee Medium
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
Accepted 72,618 Submissions 132,356
"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        if N == 0:
            return 0
        dp = [[0] * 2 for ii in range(N)]
        dp[0][1] = -prices[0] - fee
        for ii in range(1, N):
            dp[ii][0] = max(dp[ii - 1][0], dp[ii - 1][1] + prices[ii])
            dp[ii][1] = max(dp[ii - 1][1], dp[ii - 1][0] - prices[ii] - fee)
        return dp[N - 1][0]
