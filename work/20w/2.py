# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-25 12:53:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-25 13:22:00

"""
编辑距离
"""


class Solution:
    def chartWord(self, worklist: list) -> int:
        word1, word2 = worklist
        N, M = len(word1), len(word2)
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        if N == 0 or M == 0:
            return max(N, M)
        for ii in range(N + 1):
            dp[ii][0] = ii
        for jj in range(M + 1):
            dp[0][jj] = jj
        for ii in range(1, N + 1):
            for jj in range(1, M + 1):
                max_x = dp[ii - 1][jj] + 1
                max_y = dp[ii][jj - 1] + 1
                max_xy = dp[ii - 1][jj - 1]
                if word1[ii - 1] != word2[jj - 1]:
                    max_xy += 1
                dp[ii][jj] = min(max_x, max_y, max_xy)
        return dp[N][M]
