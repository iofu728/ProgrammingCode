# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-13 00:31:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-13 00:32:30

"""
79. Word Search Medium
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
Accepted 526,560 Submissions 1,468,906
"""


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x: int, y: int, flag: list, pre: str):
            if not word.startswith(pre):
                return
            if word == pre:
                self.res = True
                return
            if self.res:
                return
            for dx, dy in self.DIRS:
                xx, yy = dx + x, dy + y
                if not (0 <= xx < N) or not (0 <= yy < M) or flag[xx][yy] == 0:
                    continue
                flag[xx][yy] = 0
                dfs(xx, yy, flag, pre + board[xx][yy])
                flag[xx][yy] = 1

        N, M = len(board), len(board[0])
        self.res = False
        flag = [[1] * M for _ in range(N)]
        for ii in range(N):
            for jj in range(M):
                if board[ii][jj] == word[0]:
                    flag[ii][jj] = 0
                    dfs(ii, jj, flag, board[ii][jj])
                    flag[ii][jj] = 1
        return self.res
