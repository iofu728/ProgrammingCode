# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-08 13:56:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-08 13:57:07

"""
剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200
通过次数36,634提交次数53,762
"""


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for ii in range(1, N + 1):
            for jj in range(1, M + 1):
                dp[ii][jj] = max(dp[ii - 1][jj], dp[ii][jj - 1]) + grid[ii - 1][jj - 1]
        return dp[-1][-1]
