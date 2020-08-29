# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 17:43:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 17:53:22

"""
1219. Path with Maximum Gold Medium
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
Accepted 32,536 Submissions 49,939
"""


class Solution:
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        self.res = 0

        def dfs(x: int, y: int, v: int, done: set):
            self.res = max(self.res, v)
            for dx, dy in self.DIRS:
                xx, yy = x + dx, y + dy
                if (
                    not (0 <= xx < N)
                    or not (0 <= yy < M)
                    or (xx, yy) in done
                    or grid[xx][yy] == 0
                ):
                    continue
                done.add((xx, yy))
                dfs(xx, yy, v + grid[xx][yy], done)
                done.remove((xx, yy))

        done = set()
        for ii in range(N):
            for jj in range(M):
                zero_num = [
                    idx
                    for idx, (dx, dy) in enumerate(self.DIRS)
                    if (0 <= ii + dx < N)
                    and (0 <= jj + dy < M)
                    and grid[ii + dx][jj + dy]
                ]
                flag = len(zero_num) <= 1 or (
                    len(zero_num) == 2 and 1 in zero_num and 2 in zero_num
                )
                if grid[ii][jj] and flag:
                    done.add((ii, jj))
                    dfs(ii, jj, grid[ii][jj], done)
                    done.remove((ii, jj))
        return self.res
