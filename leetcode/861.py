# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-02 13:45:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-02 13:46:19

"""
861. Score After Flipping Matrix Medium
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
Accepted 22,723 Submissions 31,183
"""


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])
        res = 0
        for jj in range(M):
            num = 0
            for ii in range(N):
                num += A[ii][jj] ^ A[ii][0]
            res += max(num, N - num) * 2 ** (M - jj - 1)
        return res
