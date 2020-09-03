# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 01:08:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 01:08:49

"""
51. N-Queens Hard
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
Accepted 211,831 Submissions 450,480
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(u: int):
            if u == n:
                res.append(["".join(ii) for ii in edges])
                return
            for ii in range(n):
                if not col[ii] and not diag[u + ii] and not reverse_diag[n - u + ii]:
                    edges[u][ii] = "Q"
                    col[ii], diag[u + ii], reverse_diag[n - u + ii] = 1, 1, 1
                    dfs(u + 1)
                    edges[u][ii] = "."
                    col[ii], diag[u + ii], reverse_diag[n - u + ii] = 0, 0, 0

        col, diag, reverse_diag = [0] * n, [0] * 2 * n, [0] * 2 * n
        res, edges = [], [["."] * n for _ in range(n)]
        dfs(0)
        return res
