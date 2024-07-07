# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-07-07 11:48:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-07-07 11:48:37

"""
100359. 统计 X 和 Y 频数相等的子矩阵数量 显示英文描述 
通过的用户数4
尝试过的用户数11
用户总通过次数4
用户总提交次数13
题目难度Medium
给你一个二维字符矩阵 grid，其中 grid[i][j] 可能是 'X'、'Y' 或 '.'，返回满足以下条件的子矩阵数量：

包含 grid[0][0]
'X' 和 'Y' 的频数相等。
至少包含一个 'X'。
 

示例 1：

输入： grid = [["X","Y","."],["Y",".","."]]

输出： 3

解释：



示例 2：

输入： grid = [["X","X"],["X","Y"]]

输出： 0

解释：

不存在满足 'X' 和 'Y' 频数相等的子矩阵。

示例 3：

输入： grid = [[".","."],[".","."]]

输出： 0

解释：

不存在满足至少包含一个 'X' 的子矩阵。

 

提示：

1 <= grid.length, grid[i].length <= 1000
grid[i][j] 可能是 'X'、'Y' 或 '.'.
"""
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        # Grid dimensions
        rows, cols = len(grid), len(grid[0])

        # Prefix sums for X and Y
        prefixX = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefixY = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build prefix sum arrays
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefixX[i][j] = prefixX[i - 1][j] + prefixX[i][j - 1] - prefixX[i - 1][j - 1] + (grid[i - 1][j - 1] == 'X')
                prefixY[i][j] = prefixY[i - 1][j] + prefixY[i][j - 1] - prefixY[i - 1][j - 1] + (grid[i - 1][j - 1] == 'Y')

        count = 0

        # Check each submatrix starting from (0, 0) to (i, j)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                countX = prefixX[i][j]  # Total X's in submatrix from (0, 0) to (i, j)
                countY = prefixY[i][j]  # Total Y's in submatrix from (0, 0) to (i, j)

                # Check if they have equal frequency and at least one 'X'
                if countX == countY and countX > 0:
                    count += 1

        return count
