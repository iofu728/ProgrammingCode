# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-23 16:19:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-23 16:19:24

"""
100334. 包含所有 1 的最小矩形面积 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个二维 二进制 数组 grid。请你找出一个边在水平方向和竖直方向上、面积 最小 的矩形，并且满足 grid 中所有的 1 都在矩形的内部。

返回这个矩形可能的 最小 面积。

 

示例 1：

输入： grid = [[0,1,0],[1,0,1]]

输出： 6

解释：



这个最小矩形的高度为 2，宽度为 3，因此面积为 2 * 3 = 6。

示例 2：

输入： grid = [[0,0],[1,0]]

输出： 1

解释：



这个最小矩形的高度和宽度都是 1，因此面积为 1 * 1 = 1。

 

提示：

1 <= grid.length, grid[i].length <= 1000
grid[i][j] 是 0 或 1。
输入保证 grid 中至少有一个 1 。
"""
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x1, y1 = len(grid) - 1, len(grid[0]) - 1
        x2, y2 = 0, 0
        for ii in range(len(grid)):
            for jj in range(len(grid[0])):
                if grid[ii][jj] == 1:
                    x1 = min(x1, ii)
                    y1 = min(y1, jj)
                    x2 = max(x2, ii)
                    y2 = max(y2, jj)
        # print(x1, y1, x2, y2)
        return (x2 - x1 + 1) * (y2 - y1 + 1)