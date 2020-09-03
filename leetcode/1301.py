# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 11:18:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 11:22:08

"""
1301. Number of Paths with Max Score Hard
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

 

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]
 

Constraints:

2 <= board.length == board[i].length <= 100
Accepted 5,358 Submissions 14,290
"""


class Solution:
    MODS = 10 ** 9 + 7

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        def update(x: int, y: int, u: int, v: int):
            if u >= N or v >= N or dp[u][v][0] == -1:
                return
            if dp[u][v][0] > dp[x][y][0]:
                dp[x][y] = dp[u][v][:]
            elif dp[u][v][0] == dp[x][y][0]:
                dp[x][y][1] += dp[u][v][1]

        N = len(board)
        dp = [[[-1, 0]] * N for _ in range(N)]
        dp[N - 1][N - 1] = [0, 1]

        for ii in range(N - 1, -1, -1):
            for jj in range(N - 1, -1, -1):
                if ii == jj == N - 1:
                    continue
                if board[ii][jj] != "X":
                    update(ii, jj, ii + 1, jj)
                    update(ii, jj, ii, jj + 1)
                    update(ii, jj, ii + 1, jj + 1)
                    if dp[ii][jj][0] != -1:
                        dp[ii][jj][0] += (
                            0 if board[ii][jj] == "E" else int(board[ii][jj])
                        )
        t = dp[0][0]
        return [t[0], t[1] % self.MODS] if t[0] != -1 else [0, 0]
