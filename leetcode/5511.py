# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-13 10:30:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-13 10:34:20

"""
5511. 二进制矩阵中的特殊位置 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。

特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。

 

示例 1：

输入：mat = [[1,0,0],
            [0,0,1],
            [1,0,0]]
输出：1
解释：(1,2) 是一个特殊位置，因为 mat[1][2] == 1 且所处的行和列上所有其他元素都是 0
示例 2：

输入：mat = [[1,0,0],
            [0,1,0],
            [0,0,1]]
输出：3
解释：(0,0), (1,1) 和 (2,2) 都是特殊位置
示例 3：

输入：mat = [[0,0,0,1],
            [1,0,0,0],
            [0,1,1,0],
            [0,0,0,0]]
输出：2
示例 4：

输入：mat = [[0,0,0,0,0],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
输出：3
 

提示：

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] 是 0 或 1
"""


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        N, M = len(mat), len(mat[0])
        row, lines = [0] * N, [0] * M
        for ii in range(N):
            for jj in range(M):
                if mat[ii][jj]:
                    row[ii] += 1
                    lines[jj] += 1
        res = 0
        for ii in range(N):
            for jj in range(M):
                if mat[ii][jj]:
                    if row[ii] == 1 and lines[jj] == 1:
                        res += 1
        return res
