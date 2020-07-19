# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-19 00:20:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-19 00:22:28

"""
312. Burst Balloons Hard
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
Accepted 96,732 Submissions 187,986
"""


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0] * (N + 2) for _ in range(N + 2)]
        val = [1] + nums + [1]

        for ii in range(N - 1, -1, -1):
            for jj in range(ii + 2, N + 2):
                for kk in range(ii + 1, jj):
                    now = val[ii] * val[jj] * val[kk]
                    now += dp[ii][kk] + dp[kk][jj]
                    dp[ii][jj] = max(dp[ii][jj], now)
        return dp[0][N + 1]
