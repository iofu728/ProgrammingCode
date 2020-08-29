# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 16:19:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 16:20:35

"""
329. Longest Increasing Path in a Matrix Hard
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Accepted 157,320 Submissions 361,266
"""

class Solution:
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x: int, y: int):
            tmp = []
            for dx, dy in self.DIRS:
                xx, yy = x + dx, y + dy
                if not (0 <= xx < N) or not (0 <= yy < M):
                    continue
                if matrix[xx][yy] > matrix[x][y]:
                    if dp[xx][yy]:
                        tmp.append(dp[xx][yy])
                    else:
                        tmp.append(dfs(xx, yy))
            dp[x][y] = max(tmp) + 1 if tmp else 1
            self.res = max(self.res, dp[x][y])
            return dp[x][y]

        if not matrix:
            return 0
        N, M = len(matrix), len(matrix[0])
        dp = [[0] * M for _ in range(N)]
        self.res = 0
        for ii in range(N):
            for jj in range(M):
                if not dp[ii][jj]:
                    dfs(ii, jj)
        print(dp)
        return self.res
