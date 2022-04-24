# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-18 15:17:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-18 15:18:00

"""
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
Medium

766

59

Add to List

Share
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105
Accepted
23,656
Submissions
45,346
"""


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def is_ok(n):
            for ii in range(N - n + 1):
                for jj in range(M - n + 1):
                    if k[ii + n][jj + n] - k[ii + n][jj] - k[ii][jj + n] + k[ii][jj] <= threshold:
                        return True
            return False
        N, M = len(mat), len(mat[0])
        k = [[0] * (M + 1) for ii in range(N + 1)]
        for ii in range(N):
            tmp = [0] * (M + 1)
            for jj in range(M):
                tmp[jj + 1] = tmp[jj] + mat[ii][jj]
                k[ii + 1][jj + 1] = k[ii][jj + 1] + tmp[jj + 1]
        l, r = 1, min(N, M) + 2
        while l < r:
            m = (l + r) >> 1
            if is_ok(m):
                l = m + 1
            else:
                r = m
        return l - 1
