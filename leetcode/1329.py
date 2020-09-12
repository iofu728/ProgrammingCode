# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-12 23:48:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-12 23:49:05

"""
1329. Sort the Matrix Diagonally Medium
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
Accepted 19,267 Submissions 24,522
"""


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        N, M = len(mat), len(mat[0])
        for size in range(M, -N - 1, -1):
            tmp = sorted(
                [mat[ii][ii + size] for ii in range(N) if 0 <= (ii + size) < M]
            )
            idx = 0
            for ii in range(N):
                if 0 <= ii + size < M:
                    mat[ii][ii + size] = tmp[idx]
                    idx += 1
        return mat
