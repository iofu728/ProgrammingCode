# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-04 17:37:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-04 17:37:56

"""
407. Trapping Rain Water II Hard
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

Constraints:

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000
Accepted 43,356 Submissions 101,787
"""
import heapq


class Solution:
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        N, M = len(heightMap), len(heightMap[0])
        flag = [[0] * M for _ in range(N)]
        queue = []
        for ii in range(N):
            if ii in [0, N - 1]:
                for jj in range(M):
                    heapq.heappush(queue, (heightMap[ii][jj], ii, jj))
                    flag[ii][jj] = 1
            else:
                for jj in [0, M - 1]:
                    heapq.heappush(queue, (heightMap[ii][jj], ii, jj))
                    flag[ii][jj] = 1
        res = 0
        while queue:
            head, x, y = heapq.heappop(queue)
            # print(x, y, head, queue)
            for dx, dy in self.DIRS:
                xx, yy = x + dx, y + dy
                if not (0 <= xx < N) or not (0 <= yy < M) or flag[xx][yy]:
                    continue
                if head > heightMap[xx][yy]:
                    res += head - heightMap[xx][yy]
                heapq.heappush(queue, (max(heightMap[xx][yy], head), xx, yy))
                flag[xx][yy] = 1
        return res
