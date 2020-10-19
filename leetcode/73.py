# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-03 19:52:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-03 19:59:09

"""
73. Set Matrix Zeroes Medium
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
Accepted 351,460 Submissions 807,843
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lines, rows = set(), set()
        N, M = len(matrix), len(matrix[0])
        for ii in range(N):
            for jj in range(M):
                if matrix[ii][jj] == 0:
                    lines.add(ii)
                    rows.add(jj)
        for ii in lines:
            for jj in range(M):
                matrix[ii][jj] = 0
        for ii in range(N):
            for jj in rows:
                matrix[ii][jj] = 0
