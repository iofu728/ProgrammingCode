# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 19:16:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 19:17:54

"""
62. Unique Paths Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

## Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

## Example 2:

Input: m = 7, n = 3
Output: 28

## Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

Accepted 405,319 Submissions 786,349
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for ii in range(m):
            dp[0][ii] = 1
        for ii in range(1, n):
            dp[ii][0] = 1
        for ii in range(1, n):
            for jj in range(1, m):
                dp[ii][jj] = dp[ii - 1][jj] + dp[ii][jj - 1]
        return dp[n - 1][m - 1]
