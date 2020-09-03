# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 21:36:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 21:37:56

"""
37. Sudoku Solver Hard
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
Accepted 195,266 Submissions 444,423
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(x: int, y: int):
            if self.res:
                return
            if board[x][y] != ".":
                if x == 8 and y == 8:
                    self.res = True
                    return
                if y < 8:
                    dfs(x, y + 1)
                else:
                    dfs(x + 1, 0)
                return
            for s in range(1, 10):
                s = str(s)
                if (
                    not s in col[y]
                    and not s in row[x]
                    and not s in subset[x // 3][y // 3]
                ):
                    col[y].add(s)
                    row[x].add(s)
                    subset[x // 3][y // 3].add(s)
                    board[x][y] = s
                    if x == 8 and y == 8:
                        self.res = True
                        return
                    if y < 8:
                        dfs(x, y + 1)
                    else:
                        dfs(x + 1, 0)
                    if self.res:
                        return
                    col[y].remove(s)
                    row[x].remove(s)
                    subset[x // 3][y // 3].remove(s)
                    board[x][y] = "."

        col = [set() for ii in range(9)]
        row = [set() for ii in range(9)]
        subset = [[set() for ii in range(3)] for _ in range(3)]
        self.res = False
        for ii in range(9):
            for jj in range(9):
                if board[ii][jj] != ".":
                    col[jj].add(board[ii][jj])
                    row[ii].add(board[ii][jj])
                    subset[ii // 3][jj // 3].add(board[ii][jj])
        dfs(0, 0)
