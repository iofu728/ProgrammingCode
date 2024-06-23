# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-23 16:20:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-23 16:22:30

"""
100332. 包含所有 1 的最小矩形面积 II 显示英文描述 
通过的用户数3
尝试过的用户数11
用户总通过次数3
用户总提交次数16
题目难度Hard
给你一个二维 二进制 数组 grid。你需要找到 3 个 不重叠、面积 非零 、边在水平方向和竖直方向上的矩形，并且满足 grid 中所有的 1 都在这些矩形的内部。

返回这些矩形面积之和的 最小 可能值。

注意，这些矩形可以相接。

 

示例 1：

输入： grid = [[1,0,1],[1,1,1]]

输出： 5

解释：



位于 (0, 0) 和 (1, 0) 的 1 被一个面积为 2 的矩形覆盖。
位于 (0, 2) 和 (1, 2) 的 1 被一个面积为 2 的矩形覆盖。
位于 (1, 1) 的 1 被一个面积为 1 的矩形覆盖。
示例 2：

输入： grid = [[1,0,1,0],[0,1,0,1]]

输出： 5

解释：



位于 (0, 0) 和 (0, 2) 的 1 被一个面积为 3 的矩形覆盖。
位于 (1, 1) 的 1 被一个面积为 1 的矩形覆盖。
位于 (1, 3) 的 1 被一个面积为 1 的矩形覆盖。
 

提示：

1 <= grid.length, grid[i].length <= 30
grid[i][j] 是 0 或 1。
输入保证 grid 中至少有三个 1 。
"""
def minimumArea(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    min_row, max_row = m, 0
    min_col, max_col = n, 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)

    if min_row > max_row or min_col > max_col:
        return 0

    return (max_row - min_row + 1) * (max_col - min_col + 1)


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        # either it is a hamburger or a T-joint
        
        minres = len(grid) * len(grid[0])

        for _ in range(4):
        
            n = len(grid)
            m = len(grid)
            
            for x in range(1,n):
                for y in range(1,m):
                    val = 0
                    val += minimumArea([[x for x in row[:y]] for row in grid[:x]])
                    val += minimumArea([[x for x in row[y:]] for row in grid[:x]])
                    val += minimumArea([[x for x in row] for row in grid[x:]])
                    minres = min(minres, val)
                    
            for x in range(1,n):
                for y in range(x+1,n):
                    val = 0
                    val += minimumArea([[x for x in row] for row in grid[:x]])
                    val += minimumArea([[x for x in row] for row in grid[x:y]])
                    val += minimumArea([[x for x in row] for row in grid[y:]])
                    minres = min(minres, val)

            grid = list(zip(*grid[::-1]))

        return minres
        
        
        
        
