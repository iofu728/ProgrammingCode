# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-18 14:27:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-18 14:28:20

"""
97. Interleaving String Hard
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Accepted 153,511 Submissions 490,496
"""
from collections import Counter


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if Counter(s1) + Counter(s2) != Counter(s3):
            return False

        N, M, NM = [len(ii) for ii in [s1, s2, s3]]
        dp = [False] * (M + 1)
        dp[0] = True
        for ii in range(1, M + 1):
            dp[ii] = dp[ii - 1] and s2[ii - 1] == s3[ii - 1]
            if not dp[ii]:
                break

        for ii in range(1, N + 1):
            dp[0] = dp[0] and s1[ii - 1] == s3[ii - 1]
            for jj in range(1, M + 1):
                dp[jj] = (dp[jj - 1] and s2[jj - 1] == s3[ii + jj - 1]) or (
                    dp[jj] and s1[ii - 1] == s3[ii + jj - 1]
                )
        return dp[-1]
