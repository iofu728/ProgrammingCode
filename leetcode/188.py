# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-23 19:38:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-23 19:38:50

"""
188. Best Time to Buy and Sell Stock IV Hard
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Accepted 135,325 Submissions 482,720
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        if N == 0:
            return 0
        if k > N // 2:
            dp0, dp1 = 0, -prices[0]
            for ii in range(1, N):
                tmp = dp0
                dp0 = max(dp0, dp1 + prices[ii])
                dp1 = max(dp1, tmp - prices[ii])
            return max(dp0, dp1)

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(N)]
        for ii in range(N):
            for jj in range(k, 0, -1):
                if ii == 0:
                    dp[ii][jj][1] = -prices[ii]
                    continue
                dp[ii][jj][0] = max(dp[ii - 1][jj][0], dp[ii - 1][jj][1] + prices[ii])
                dp[ii][jj][1] = max(
                    dp[ii - 1][jj][1], dp[ii - 1][jj - 1][0] - prices[ii]
                )
        return dp[N - 1][k][0]
