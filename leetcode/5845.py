# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-08-15 13:40:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-08-15 13:40:49

"""
5845. 你能穿过矩阵的最后一天 显示英文描述 
通过的用户数200
尝试过的用户数277
用户总通过次数211
用户总提交次数375
题目难度Hard
给你一个下标从 1 开始的二进制矩阵，其中 0 表示陆地，1 表示水域。同时给你 row 和 col 分别表示矩阵中行和列的数目。

一开始在第 0 天，整个 矩阵都是 陆地 。但每一天都会有一块新陆地被 水 淹没变成水域。给你一个下标从 1 开始的二维数组 cells ，其中 cells[i] = [ri, ci] 表示在第 i 天，第 ri 行 ci 列（下标都是从 1 开始）的陆地会变成 水域 （也就是 0 变成 1 ）。

你想知道从矩阵最 上面 一行走到最 下面 一行，且只经过陆地格子的 最后一天 是哪一天。你可以从最上面一行的 任意 格子出发，到达最下面一行的 任意 格子。你只能沿着 四个 基本方向移动（也就是上下左右）。

请返回只经过陆地格子能从最 上面 一行走到最 下面 一行的 最后一天 。

 

示例 1：


输入：row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
输出：2
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 2 天。
示例 2：


输入：row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
输出：1
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 1 天。
示例 3：


输入：row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
输出：3
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 3 天。
 

提示：

2 <= row, col <= 2 * 104
4 <= row * col <= 2 * 104
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
cells 中的所有格子坐标都是 唯一 的。
"""


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        low, high = 0, row * col
        a = [[0 for i in range(col)] for j in range(row)]
        for i in range(row * col):
            a[cells[i][0] - 1][cells[i][1] - 1] = i + 1
        while low != high:
            mid = (low + high + 1) >> 1
            seen = [[False for i in range(col)] for j in range(row)]

            def dfs(x, y):
                seen[x][y] = True
                for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if (
                        0 <= i < row
                        and 0 <= j < col
                        and a[i][j] > mid
                        and not seen[i][j]
                    ):
                        dfs(i, j)

            for i in range(col):
                if a[0][i] > mid and not seen[0][i]:
                    dfs(0, i)
            if any(seen[-1]):
                low = mid
            else:
                high = mid - 1
        return low