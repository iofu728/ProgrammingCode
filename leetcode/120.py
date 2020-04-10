# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-10 22:42:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-10 22:49:52

"""
120. Triangle Medium
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Accepted 229,261 Submissions 536,488
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        for ii in range(N - 2, -1, -1):
            for jj in range(len(triangle[ii])):
                triangle[ii][jj] += min(triangle[ii + 1][jj : jj + 2])
        return triangle[0][0]
