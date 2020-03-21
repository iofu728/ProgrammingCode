# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 20:30:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 20:52:48

"""
59. Spiral Matrix II Medium

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

## Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Accepted 176,006 Submissions 341,326
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        def one_loop(b: int, index: int):
            # print(b, index)
            if 2 * b + 1 > n:
                return
            e = n - b - 1
            for ii in range(b, e + 1):
                matrix[b][ii] = index
                index += 1
            for ii in range(b + 1, e):
                matrix[ii][e] = index
                index += 1
            if b != e:
                for ii in range(e, b - 1, -1):
                    matrix[e][ii] = index
                    index += 1
            for ii in range(e - 1, b, -1):
                matrix[ii][b] = index
                index += 1
            one_loop(b + 1, index)

        one_loop(0, 1)
        return matrix
