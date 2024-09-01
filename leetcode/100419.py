# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-09-01 12:46:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-09-01 12:47:14

"""
100419. 选择矩阵中单元格的最大得分 显示英文描述 
通过的用户数1
尝试过的用户数18
用户总通过次数1
用户总提交次数23
题目难度Hard
给你一个由正整数构成的二维矩阵 grid。

你需要从矩阵中选择 一个或多个 单元格，选中的单元格应满足以下条件：

所选单元格中的任意两个单元格都不会处于矩阵的 同一行。
所选单元格的值 互不相同。
你的得分为所选单元格值的总和。

返回你能获得的 最大 得分。

 

示例 1：

输入： grid = [[1,2,3],[4,3,2],[1,1,1]]

输出： 8

解释：



选择上图中用彩色标记的单元格，对应的值分别为 1、3 和 4 。

示例 2：

输入： grid = [[8,7,6],[8,3,2]]

输出： 15

解释：



选择上图中用彩色标记的单元格，对应的值分别为 7 和 8 。

 

提示：

1 <= grid.length, grid[i].length <= 10
1 <= grid[i][j] <= 100
"""
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        @cache
        def dp(mask, maxi):
            if not mask or not maxi:
                return 0
            res = 0
            for i in range(n):
                if mask & (1 << i):
                    if (j := idx[i][maxi]) >= 0:
                        t = dp(mask ^ (1 << i), grid[i][j] - 1) + grid[i][j]
                    else:
                        t = dp(mask ^ (1 << i), maxi)
                    res = max(res, t)
            return res

        n = len(grid)
        m = 101
        idx = [[-1] * m for _ in range(n)]
        for i in range(n):
            grid[i].sort()
            for j,val in enumerate(grid[i]):
                idx[i][val] = j
            for j in range(1, m):
                if idx[i][j] < 0:
                    idx[i][j] = idx[i][j-1]
            prev = -1
        M = 1 << n
        return dp(M - 1, m - 1)
