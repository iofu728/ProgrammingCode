# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-27 23:44:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-28 00:25:08

"""
1143. Longest Common Subsequence Medium
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

## Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

## Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

## Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

## Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

Accepted 43,217 Submissions 74,902
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        if N == 0 or M == 0:
            return 0
        dp = [[0 for _ in range(M)] for _ in range(N)]
        for jj in range(M):
            for ii in range(N):

                max_x = 0 if ii == 0 else dp[ii - 1][jj]
                max_y = 0 if jj == 0 else dp[ii][jj - 1]
                max_xy = 0 if jj == 0 or ii == 0 else dp[ii - 1][jj - 1]
                if text1[ii] == text2[jj]:
                    dp[ii][jj] = max_xy + 1
                else:
                    dp[ii][jj] = max(max_x, max_y)
        print(dp)
        return dp[N - 1][M - 1]
