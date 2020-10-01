# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-01 00:03:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-01 00:12:22


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        N = len(leaves)
        dp = [[0] * 3 for _ in range(N)]
        dp[0][0] = leaves[0] == "y"
        dp[0][1] = dp[0][2] = dp[1][2] = float("inf")
        for ii in range(1, N):
            dp[ii][0] = dp[ii - 1][0] + (leaves[ii] == "y")
            dp[ii][1] = min(dp[ii - 1][:2]) + (leaves[ii] == "r")
            dp[ii][2] = min(dp[ii - 1][1:]) + (leaves[ii] == "y")
        return dp[-1][2]
