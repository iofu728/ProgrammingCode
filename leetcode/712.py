# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 17:22:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 17:22:42


"""
712. Minimum ASCII Delete Sum for Two Strings Medium
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
Accepted 37,001 Submissions 63,183
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for ii in range(N - 1, -1, -1):
            dp[ii][M] = dp[ii + 1][M] + ord(s1[ii])
        for jj in range(M - 1, -1, -1):
            dp[N][jj] = dp[N][jj + 1] + ord(s2[jj])
        for ii in range(N - 1, -1, -1):
            for jj in range(M - 1, -1, -1):
                if s1[ii] == s2[jj]:
                    dp[ii][jj] = dp[ii + 1][jj + 1]
                else:
                    dp[ii][jj] = min(
                        dp[ii + 1][jj] + ord(s1[ii]), dp[ii][jj + 1] + ord(s2[jj])
                    )
        return dp[0][0]
