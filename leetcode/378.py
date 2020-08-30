# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 00:02:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 00:03:42

"""
378. Kth Smallest Element in a Sorted Matrix Medium
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

Accepted 199,695 Submissions 366,357
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def cal_num(tgt: int) -> int:
            ii, jj, num = N - 1, 0, 0
            while ii >= 0 and jj < N:
                if matrix[ii][jj] <= mid:
                    num += ii + 1
                    jj += 1
                else:
                    ii -= 1
            return num >= k

        N = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if cal_num(mid):
                right = mid
            else:
                left = mid + 1
        return left
