# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-06-20 11:40:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-20 11:40:37

"""
5791. 统计子岛屿 显示英文描述 
通过的用户数1
尝试过的用户数1
用户总通过次数1
用户总提交次数1
题目难度Medium
给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向 （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。

如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，那么我们称 grid2 中的这个岛屿为 子岛屿 。

请你返回 grid2 中 子岛屿 的 数目 。

 

示例 1：


输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
输出：3
解释：如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
示例 2：


输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
输出：2 
解释：如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
 

提示：

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] 和 grid2[i][j] 都要么是 0 要么是 1 。
"""


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        N, M = len(grid1), len(grid1[0])
        flags = [[0] * M for _ in range(N)]
        self.a = True

        def dfs(x, y):
            flags[x][y] = True
            if grid1[x][y] == 0:
                self.a = False
            for dx, dy in self.DIRS:
                xx, yy = dx + x, dy + y
                if 0 <= xx < N and 0 <= yy < M and grid2[xx][yy] and not flags[xx][yy]:
                    dfs(xx, yy)

        res = 0
        for ii in range(N):
            for jj in range(M):
                if grid2[ii][jj] and not flags[ii][jj]:
                    self.a = True
                    dfs(ii, jj)
                    if self.a:
                        res += 1
        return res
