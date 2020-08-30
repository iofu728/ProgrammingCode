# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 10:56:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 12:16:12

"""
5501. 使陆地分离的最少天数 显示英文描述 
通过的用户数150
尝试过的用户数218
用户总通过次数151
用户总提交次数325
题目难度Medium
给你一个由若干 0 和 1 组成的二维网格 grid ，其中 0 表示水，而 1 表示陆地。岛屿由水平方向或竖直方向上相邻的 1 （陆地）连接形成。

如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。

一天内，可以将任何单个陆地单元（1）更改为水单元（0）。

返回使陆地分离的最少天数。

 

示例 1：



输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
输出：2
解释：至少需要 2 天才能得到分离的陆地。
将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。
示例 2：

输入：grid = [[1,1]]
输出：2
解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
示例 3：

输入：grid = [[1,0,1,0]]
输出：0
示例 4：

输入：grid = [[1,1,0,1,1],
             [1,1,1,1,1],
             [1,1,0,1,1],
             [1,1,0,1,1]]
输出：1
示例 5：

输入：grid = [[1,1,0,1,1],
             [1,1,1,1,1],
             [1,1,0,1,1],
             [1,1,1,1,1]]
输出：2
 

提示：

1 <= grid.length, grid[i].length <= 30
grid[i][j] 为 0 或 1
"""


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def check(g):
            self.dp = [[1] * M for _ in range(N)]
            res = 0
            for ii in range(N):
                for jj in range(M):
                    if g[ii][jj] == 1 and self.dp[ii][jj] == 1:
                        dfs(g, ii, jj)
                        res += 1
            return res != 1

        def dfs(g: list, x: int, y: int):
            self.dp[x][y] = 0
            tmp = []
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy = dx + x, dy + y
                if (
                    not (0 <= xx < N)
                    or not (0 <= yy < M)
                    or g[xx][yy] == 0
                    or self.dp[xx][yy] == 0
                ):
                    tmp.append(0)
                    continue
                tmp.append(dfs(g, xx, yy))
            return sum(tmp) + 1

        N, M = len(grid), len(grid[0])
        self.dp = [[1] * M for _ in range(N)]
        if check(grid):
            return 0
        for ii in range(N):
            for jj in range(M):
                if grid[ii][jj] == 1:
                    grid[ii][jj] = 0
                    if check(grid):
                        return 1
                    grid[ii][jj] = 1
        return 2

