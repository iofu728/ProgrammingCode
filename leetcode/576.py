# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 23:22:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 23:23:33

"""
576. Out of Boundary Paths Medium
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

 

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
Accepted 29,775 Submissions 84,490
"""


class Solution:
    MODS = 10 ** 9 + 7

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[0] * (n + 2) for _ in range(m + 2)]
        tmp = [[0] * (n + 2) for _ in range(m + 2)]
        dp[i + 1][j + 1] = 1
        res = 0

        for kk in range(N):
            for ii in range(1, m + 1):
                res += dp[ii][1] + dp[ii][-2]
            for ii in range(1, n + 1):
                res += dp[1][ii] + dp[-2][ii]
            for ii in range(1, m + 1):
                for jj in range(1, n + 1):
                    tmp[ii][jj] = (
                        dp[ii - 1][jj]
                        + dp[ii + 1][jj]
                        + dp[ii][jj - 1]
                        + dp[ii][jj + 1]
                    )
            for ii in range(m + 2):
                for jj in range(n + 2):
                    dp[ii][jj] = tmp[ii][jj]
        return res % self.MODS
