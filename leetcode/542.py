# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-15 14:16:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-15 14:17:14

"""
542. 01 Matrix Medium
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
Accepted 73,527 Submissions 189,804
"""


class Solution:
    MAX = 2 ** 32

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        N, M = len(matrix), len(matrix[0])
        dp = [[self.MAX if matrix[ii][jj] else 0 for jj in range(M)] for ii in range(N)]
        for ii in range(N):
            for jj in range(M):
                if ii > 0:
                    dp[ii][jj] = min(dp[ii][jj], dp[ii - 1][jj] + 1)
                if jj > 0:
                    dp[ii][jj] = min(dp[ii][jj], dp[ii][jj - 1] + 1)
        for ii in range(N - 1, -1, -1):
            for jj in range(M - 1, -1, -1):
                if ii < N - 1:
                    dp[ii][jj] = min(dp[ii][jj], dp[ii + 1][jj] + 1)
                if jj < M - 1:
                    dp[ii][jj] = min(dp[ii][jj], dp[ii][jj + 1] + 1)
        return dp
