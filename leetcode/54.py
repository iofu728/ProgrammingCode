# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 20:29:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 20:30:20

"""
54. Spiral Matrix Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Accepted 324,330 Submissions 986,430
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        def one_loop(M: List[List[int]]):
            # print(M, result)
            if not len(M):
                return
            result.extend(M[0])
            result.extend([ii[-1] for ii in M[1:-1]])
            if len(M) > 1:
                result.extend(M[-1][::-1])
            if len(M[0]) > 1:
                result.extend([ii[0] for ii in M[1:-1][::-1]])
            one_loop([ii[1:-1] for ii in M[1:-1] if len(ii) > 2])

        one_loop(matrix)
        return result
