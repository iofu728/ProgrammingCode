# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-06 14:38:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-06 14:39:10

"""
891. Sum of Subsequence Widths Hard
Given an array of integers A, consider all non-empty subsequences of A.

For any sequence S, let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A. 

As the answer may be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= 20000
Accepted 9,021 Submissions 27,861
"""


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        N = len(A)
        A = sorted(A)
        MODS = 10 ** 9 + 7
        pow2, res = [1], 0
        for ii in range(1, N):
            pow2.append(2 * pow2[-1] % MODS)
        for ii, jj in enumerate(A):
            res = (res + (pow2[ii] - pow2[N - ii - 1]) * jj) % MODS
        return res
