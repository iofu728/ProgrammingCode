# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-20 10:41:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-20 11:03:28

"""
200. Number of Islands Medium
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3

Accepted 644,605 Submissions 1,410,762
"""


class Solution:
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        if not len(grid) or not len(grid[0]):
            return 0
        N, M = len(grid), len(grid[0])

        def dfs(x: int, y: int):
            if x < 0 or x >= N or y < 0 or y >= M or self.grid[x][y] == "0":
                return
            self.grid[x][y] = 0
            for dx, dy in self.DIR:
                xx, yy = x + dx, y + dy
                if N > xx >= 0 and 0 <= yy < M and self.grid[xx][yy] == "1":
                    dfs(x + dx, y + dy)

        res = 0
        for x in range(N):
            for y in range(M):
                if self.grid[x][y] == "1":
                    res += 1
                    dfs(x, y)
        return res
