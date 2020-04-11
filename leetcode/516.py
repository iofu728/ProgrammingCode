# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-11 00:35:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-11 00:36:24

"""
516. Longest Palindromic Subsequence Medium
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
Accepted 99,775 Submissions 195,253
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for ii in range(N - 1, -1, -1):
            dp[ii][ii] = 1
            for jj in range(ii + 1, N):
                if s[ii] == s[jj]:
                    dp[ii][jj] = dp[ii + 1][jj - 1] + 2
                else:
                    dp[ii][jj] = max(dp[ii + 1][jj], dp[ii][jj - 1])
        return dp[0][N - 1]
