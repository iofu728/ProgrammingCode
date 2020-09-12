# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-12 00:24:18
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-12 00:27:13

"""
959. Regions Cut By Slashes Medium
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

 

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

 

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
Accepted 20,648 Submissions 31,139
"""
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def getRoot(r: list, p: int):
            q = r[p]
            while p != r[p]:
                p = r[p]
            while q != r[p]:
                tmp = r[q]
                r[q] = p
                q = tmp
            return p
        def union(r, u, v):
            u, v = getRoot(r, u), getRoot(r, v)
            r[u] = v
            return r
        N = len(grid)
        r = list(range(4 * N * N))
        for ii in range(N):
            for jj in range(N):
                tmp = grid[ii][jj]
                root = 4 * (ii * N + jj)
                if tmp in "/ ":
                    r = union(r, root + 0, root + 1)
                    r = union(r, root + 2, root + 3)
                if tmp in "\ ":
                    r = union(r, root + 1, root + 2)
                    r = union(r, root + 0, root + 3)
                if ii < N - 1:
                    r = union(r, root + 3, root + 4 * N + 1)
                if ii:
                    r = union(r, root + 1, root - 4 * N + 3)
                if jj < N - 1:
                    r = union(r, root + 2, root + 4 + 0)
                if jj:
                    r = union(r, root + 0, root - 4 + 2)
        return len([1 for ii in range(4 * N * N) if getRoot(r, ii) == ii])
