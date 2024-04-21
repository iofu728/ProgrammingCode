# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-04-21 10:58:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-04-21 10:58:24

"""
100290. 使矩阵满足条件的最少操作次数 显示英文描述 
通过的用户数0
尝试过的用户数4
用户总通过次数0
用户总提交次数6
题目难度Medium
给你一个大小为 m x n 的二维矩形 grid 。每次 操作 中，你可以将 任一 格子的值修改为 任意 非负整数。完成所有操作后，你需要确保每个格子 grid[i][j] 的值满足：

如果下面相邻格子存在的话，它们的值相等，也就是 grid[i][j] == grid[i + 1][j]（如果存在）。
如果右边相邻格子存在的话，它们的值不相等，也就是 grid[i][j] != grid[i][j + 1]（如果存在）。
请你返回需要的 最少 操作数目。

 

示例 1：

输入：grid = [[1,0,2],[1,0,2]]

输出：0

解释：



矩阵中所有格子已经满足要求。

示例 2：

输入：grid = [[1,1,1],[0,0,0]]

输出：3

解释：



将矩阵变成 [[1,0,1],[1,0,1]] ，它满足所有要求，需要 3 次操作：

将 grid[1][0] 变为 1 。
将 grid[0][1] 变为 0 。
将 grid[1][2] 变为 1 。
示例 3：

输入：grid = [[1],[2],[3]]

输出：2

解释：



这个矩阵只有一列，我们可以通过 2 次操作将所有格子里的值变为 1 。

 

提示：

1 <= n, m <= 1000
0 <= grid[i][j] <= 9

"""
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dp = [[float("inf")]*10  for ii in range(M)]
        for ii in range(M):
            c = Counter([grid[jj][ii] for jj in range(N)])
            for jj in range(10):
                dp[ii][jj] = min([dp[ii - 1][kk] if ii > 0 else 0 for kk in range(10) if kk != jj]) + N - c[jj]
        return min(dp[-1])