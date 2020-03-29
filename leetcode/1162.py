# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 00:31:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 01:21:28

"""
1162. As Far from Land as Possible Medium
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

## Example 1:
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

## Example 2:
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.

## Note:
1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
Accepted 12,324 Submissions 29,439
"""


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N, MAX, max_num = len(grid), 2 ** 16, -1
        dp = [[0 for _ in range(N)] for _ in range(N)]

        for ii in range(N):
            for jj in range(N):
                if grid[ii][jj] == 1:
                    continue
                a1 = MAX if not ii else dp[ii - 1][jj]
                a2 = MAX if not jj else dp[ii][jj - 1]
                dp[ii][jj] = min(a1, a2) + 1

        for ii in range(N - 1, -1, -1):
            for jj in range(N - 1, -1, -1):
                if grid[ii][jj] == 1:
                    continue
                a1 = MAX if ii == N - 1 else dp[ii + 1][jj]
                a2 = MAX if jj == N - 1 else dp[ii][jj + 1]
                a3 = MAX if not ii else dp[ii - 1][jj]
                a4 = MAX if not jj else dp[ii][jj - 1]
                dp[ii][jj] = min(a1, a2, a3, a4) + 1
                tmp = dp[ii][jj]
                if tmp > max_num:
                    max_num = tmp
        if max_num >= MAX:
            max_num = -1
        return max_num
