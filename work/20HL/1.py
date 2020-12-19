# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-11-05 21:19:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-11-05 21:41:42

class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def maxArea(self, matrix):
        N, M = len(matrix), len(matrix[0])
        queue = []
        flags = [[False] * M for _ in range(N)]
        res = 0
        for ii in range(N):
            for jj in range(M):
                if flags[ii][jj] == False and matrix[ii][jj]:
                    queue.append((ii, jj))
                    flags[ii][jj] = True
                tmp = 0
                while queue:
                    x, y = queue.pop(0)
                    tmp += matrix[x][y]
                    for dx, dy in self.DIRS:
                        xx, yy = dx + x, dy + y
                        if not (0 <= xx < N and 0 <= yy < M) or flags[xx][yy] == True or matrix[xx][yy] == 0:
                            continue
                        flags[xx][yy] = True
                        queue.append((xx, yy))
                res = max(res, tmp)
        return res


        