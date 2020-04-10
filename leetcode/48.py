# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-07 21:34:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-07 21:48:08

"""
48. Rotate Image Medium

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
Accepted 362,485 Submissions 669,127
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for ii in range(N // 2):
            for jj in range(N):
                matrix[ii][jj], matrix[N - ii - 1][jj] = (
                    matrix[N - ii - 1][jj],
                    matrix[ii][jj],
                )
        for ii in range(N):
            for jj in range(ii):
                matrix[ii][jj], matrix[jj][ii] = matrix[jj][ii], matrix[ii][jj]
