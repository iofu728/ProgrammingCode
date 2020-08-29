# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-21 22:08:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-21 22:08:16

import sys

sys.setrecursionlimit(1000000)


class Solution:
    DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        b = board.copy()
        N, M = len(b), len(b[0])

        def dfs(x: int, y: int):

            num = 0
            for dx, dy in self.DIRS:
                xx = x + dx
                yy = y + dy
                if not (0 <= xx < N) or not (0 <= yy < M):
                    continue
                num += board[xx][yy] == "M"
            # print(x, y, num, b)
            if num > 0:
                b[x][y] = str(num)
            else:
                b[x][y] = "B"
                for dx, dy in self.DIRS:
                    xx = x + dx
                    yy = y + dy
                    if not (0 <= xx < N) or not (0 <= yy < M):
                        continue
                    if b[xx][yy] != "E":
                        continue
                    dfs(xx, yy)

        xx, yy = click
        if b[xx][yy] == "M":
            b[xx][yy] = "X"
        else:
            dfs(xx, yy)
        return b

