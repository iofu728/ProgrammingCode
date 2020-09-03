# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-03 15:17:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-03 15:18:28

"""
74. Search a 2D Matrix Medium
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
Accepted 343,610 Submissions 939,001
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        N, M = len(matrix), len(matrix[0])
        left, right = 0, N * M - 1
        while left <= right:
            mid = (left + right) >> 1
            x, y = mid // M, mid % M
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

