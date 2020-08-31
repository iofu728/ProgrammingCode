# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 22:43:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 22:44:17

"""
931. Minimum Falling Path Sum Medium
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Constraints:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
Accepted 53,374 Submissions 85,273
"""
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = A[-1]
        N = len(A)
        for ii in range(N - 2, -1, -1):
            # print(ii, dp)
            tmp = dp.copy()
            for jj in range(N):
                tmp[jj] = A[ii][jj] + min(dp[max(jj - 1, 0): jj + 2])
            dp = tmp
        return min(dp)
