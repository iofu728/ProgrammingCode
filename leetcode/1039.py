# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-11 00:57:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-11 00:58:26

"""
1039. Minimum Score Triangulation of Polygon Medium
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:

Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
Example 3:

Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
 

Note:

3 <= A.length <= 50
1 <= A[i] <= 100
Accepted 7,113 Submissions 15,131
"""


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A) - 1
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for ii in range(2, N + 1):
            for jj in range(1, N - ii + 2):
                k = jj + ii - 1
                dp[jj][k] = dp[jj][jj] + dp[jj + 1][k] + A[jj - 1] * A[jj] * A[k]
                for m in range(jj + 1, k):
                    dp[jj][k] = min(
                        dp[jj][k], dp[jj][m] + dp[m + 1][k] + A[jj - 1] * A[m] * A[k]
                    )
        return dp[1][N]
