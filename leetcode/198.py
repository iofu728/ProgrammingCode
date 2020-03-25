# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-25 12:48:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-25 12:50:52

"""
198. House Robber Easy

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

## Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

## Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
Accepted 453,499 Submissions 1,088,971
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if not N:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(N)]
        dp[0][1] = nums[0]
        for ii in range(1, N):
            dp[ii][0] = max(dp[ii - 1])
            dp[ii][1] = dp[ii - 1][0] + nums[ii]
        return max(dp[N - 1])
