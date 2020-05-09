# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-08 12:02:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-08 12:03:14

"""
221. 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
通过次数39,446提交次数96,293
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if N == 0:
            return 0
        M = len(matrix[0])
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        res = 0
        for ii in range(1, N + 1):
            for jj in range(1, M + 1):
                if matrix[ii - 1][jj - 1] == "0":
                    continue
                dp[ii][jj] = min(dp[ii][jj - 1], dp[ii - 1][jj], dp[ii - 1][jj - 1]) + 1
                if dp[ii][jj] > res:
                    res = dp[ii][jj]
        return res ** 2
