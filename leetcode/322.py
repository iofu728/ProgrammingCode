# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-27 13:18:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-27 19:29:19

"""
322. Coin Change Medium

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

## Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

## Example 2:
Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

Accepted 335,526 Submissions 990,565
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for ii in range(coin, amount + 1):
                dp[ii] = min(dp[ii], dp[ii - coin] + 1)
        # print(dp)
        return dp[amount] if dp[amount] != amount + 1 else -1