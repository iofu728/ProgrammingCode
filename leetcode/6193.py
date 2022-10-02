# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-02 12:55:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-02 12:55:43

"""
6193. 沙漏的最大总和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个大小为 m x n 的整数矩阵 grid 。

按以下形式将矩阵的一部分定义为一个 沙漏 ：


返回沙漏中元素的 最大 总和。

注意：沙漏无法旋转且必须整个包含在矩阵中。

 

示例 1：


输入：grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
输出：30
解释：上图中的单元格表示元素总和最大的沙漏：6 + 2 + 1 + 2 + 9 + 2 + 8 = 30 。
示例 2：


输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
输出：35
解释：上图中的单元格表示元素总和最大的沙漏：1 + 2 + 3 + 5 + 7 + 8 + 9 = 35 。
 

提示：

m == grid.length
n == grid[i].length
3 <= m, n <= 150
0 <= grid[i][j] <= 106
"""
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def get_x(x):
            return sum([grid[x][ii] for ii in range(3)]) + grid[x + 1][1] + sum([grid[x + 2][ii] for ii in range(3)])
        N, M = len(grid), len(grid[0])
        res = 0
        for ii in range(N - 2):
            tmp = get_x(ii)
            res = max(res, tmp)
            for jj in range(1, M - 2):
                tmp = tmp - grid[ii][jj - 1] - grid[ii + 1][jj] - grid[ii + 2][jj - 1] + grid[ii][jj + 2] + grid[ii + 1][jj + 1] + grid[ii + 2][jj + 2]
                res = max(res, tmp)
        return res
            