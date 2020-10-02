# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-02 16:21:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-02 16:24:03

"""
63. Unique Paths II Medium
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Accepted 319,591 Submissions 918,339
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp1, dp2 = [0] * (M + 1), [0] * (M + 1)
        dp2[0] = 1
        for ii in range(1, N + 1):
            for jj in range(1, M + 1):
                if obstacleGrid[ii - 1][jj - 1]:
                    continue
                dp2[jj] = dp1[jj] + dp2[jj - 1]
            dp1, dp2 = dp2, [0] * (M + 1)
        return dp1[-1]
