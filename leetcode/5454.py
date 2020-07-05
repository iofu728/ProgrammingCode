# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-05 11:17:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-05 12:27:55

"""
5454. 统计全 1 子矩形 显示英文描述 
通过的用户数419
尝试过的用户数670
用户总通过次数420
用户总提交次数865
题目难度Medium
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

 

示例 1：

输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。
示例 2：

输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21
示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5
 

提示：

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        N, M = len(mat), len(mat[0])
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        res = 0
        for ii in range(1, N + 1):
            for jj in range(1, M + 1):
                dp[ii][jj] = (
                    dp[ii - 1][jj]
                    + dp[ii][jj - 1]
                    - dp[ii - 1][jj - 1]
                    + mat[ii - 1][jj - 1]
                )
        for ii in range(N):
            for jj in range(M):
                for kk in range(N - ii):
                    for ll in range(M - jj):
                        if dp[ii + kk + 1][jj + ll + 1] - dp[ii][jj + ll + 1] - dp[
                            ii + kk + 1
                        ][jj] + dp[ii][jj] == (kk + 1) * (ll + 1):
                            res += 1
                        else:
                            break
        return res
