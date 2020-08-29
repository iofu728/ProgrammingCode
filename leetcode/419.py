# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 21:37:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 21:38:50

"""
419. Battleships in a Board Medium
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

Accepted 98,162 Submissions 139,896
"""


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(x: int, y: int):
            dp[x][y] = 1
            # print(x, y)
            if x + 1 < N and board[x + 1][y] == "X":
                # print(x, y, 1111)
                x += 1
                while x < N and dp[x][y] == 0 and board[x][y] == "X":
                    dp[x][y] = 1
                    x += 1
            elif y + 1 < M and board[x][y + 1] == "X":
                # print(x, y, 2222)
                y += 1
                while y < M and dp[x][y] == 0 and board[x][y] == "X":
                    dp[x][y] = 1
                    y += 1

        N, M = len(board), len(board[0])
        dp = [[0] * M for _ in range(N)]
        res = 0
        for ii in range(N):
            for jj in range(M):
                if board[ii][jj] == "X" and dp[ii][jj] == 0:
                    dfs(ii, jj)
                    res += 1
        return res
