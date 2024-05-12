# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-12 12:05:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-12 12:06:09

"""
100281. 矩阵中的最大得分 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个由 正整数 组成、大小为 m x n 的矩阵 grid。你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为 c1 的单元格移动到值为 c2 的单元格的得分为 c2 - c1 。

你可以从 任一 单元格开始，并且必须至少移动一次。

返回你能得到的 最大 总得分。

 

示例 1：


输入：grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]

输出：9

解释：从单元格 (0, 1) 开始，并执行以下移动：
- 从单元格 (0, 1) 移动到 (2, 1)，得分为 7 - 5 = 2 。
- 从单元格 (2, 1) 移动到 (2, 2)，得分为 14 - 7 = 7 。
总得分为 2 + 7 = 9 。

示例 2：



输入：grid = [[4,3,2],[3,2,1]]

输出：-1

解释：从单元格 (0, 0) 开始，执行一次移动：从 (0, 0) 到 (0, 1) 。得分为 3 - 4 = -1 。

 

提示：

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 105

"""
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[-1])
        pre = [-float("inf")] * M
        res = -float("inf")
        for ii in range(N - 1, -1, -1):
            tmp = [-float("inf")] * M
            for jj in range(M - 1, -1, -1):
                ref = pre[jj]
                if jj != M - 1:
                    ref = max(ref, tmp[jj + 1])
                res = max(res, ref - grid[ii][jj])
                tmp[jj] = max(grid[ii][jj], pre[jj])
                if jj != M - 1:
                    tmp[jj] = max(tmp[jj], tmp[jj + 1])
            pre = tmp
        return res
                