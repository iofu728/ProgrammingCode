# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-02 00:12:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-02 00:58:19

"""
289. Game of Life Medium
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

## Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

## Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Accepted 162,713 Submissions 312,712
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        T = [
            (ii, jj) for ii in range(-1, 2) for jj in range(-1, 2) if (ii, jj) != (0, 0)
        ]
        t = [ii[:] for ii in board]

        def get_life(x: int, y: int):
            if x < 0 or x >= M or y < 0 or y >= N:
                return None
            return t[x][y]

        def get_neighbor(x: int, y: int):
            ne = [get_life(ii + x, jj + y) for ii, jj in T]
            ne_num = len([1 for ii in ne if ii])
            now = t[x][y]
            if now:
                return int(ne_num in [2, 3])
            return int(ne_num == 3)

        for ii in range(M):
            for jj in range(N):
                board[ii][jj] = get_neighbor(ii, jj)
