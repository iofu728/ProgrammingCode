# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-24 22:32:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-24 22:33:41

"""
317. Shortest Distance from All Buildings
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

通过次数2,825提交次数5,956
"""


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            flag = [[0] * M for ii in range(N)]
            c, dis, d = 0, 0, 0
            queue = [(x, y)]
            while queue:
                d += 1
                for _ in range(len(queue)):
                    ii, jj = queue.pop(0)
                    for dx, dy in self.DIRS:
                        xx, yy = ii + dx, jj + dy
                        if 0 <= xx < N and 0 <= yy < M and flag[xx][yy] == 0:
                            flag[xx][yy] = 1
                            if grid[xx][yy] == 0:
                                queue.append((xx, yy))
                            elif grid[xx][yy] == 1:
                                c += 1
                                dis += d
            return dis if c == B else float("inf")

        N, M = len(grid), len(grid[0])
        B = len([1 for ii in range(N) for jj in range(M) if grid[ii][jj] == 1])
        res = float("inf")
        for ii in range(N):
            for jj in range(M):
                if grid[ii][jj] == 0:
                    res = min(res, bfs(ii, jj))
        return res if res != float("inf") else -1
