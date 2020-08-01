# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-31 00:09:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-31 00:10:09

"""
85. Maximal Rectangle Hard
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
Accepted 180,841 Submissions 480,722
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        N, M = len(matrix), len(matrix[0])

        def getMaxHeightsArea(heights):
            stack, res = [-1], 0
            for ii in range(M):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[ii]:
                    res = max(res, heights[stack.pop()] * (ii - stack[-1] - 1))
                stack.append(ii)
            while stack[-1] != -1:
                res = max(res, heights[stack.pop()] * (M - stack[-1] - 1))
            return res

        res = 0
        dp = [0] * M
        for ii in range(N):
            for jj in range(M):
                dp[jj] = dp[jj] + 1 if matrix[ii][jj] == "1" else 0
            res = max(res, getMaxHeightsArea(dp))
        return res
