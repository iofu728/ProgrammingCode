# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-03 20:45:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-03 20:46:12

"""
121. Best Time to Buy and Sell Stock Easy
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Accepted 796,534 Submissions 1,597,304
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if not N:
            return 0
        dp = [0] * N
        for idx in range(1, N):
            tmp = min(prices[:idx])
            dp[idx] = max(0, prices[idx] - tmp)
        return max(dp)
