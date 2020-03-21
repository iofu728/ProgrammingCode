# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 14:11:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 14:52:11

"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
通过次数210,718提交次数726,086
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        M = len(s)
        dp = [[False] * M for _ in range(M)]
        for i in range(M):
            dp[i][i] = True
        begin, end = 0, 0
        for jj in range(2, M + 1):
            for b in range(M - jj + 1):
                e = b + jj - 1
                # print(b, e)
                if s[b] == s[e]:
                    if b + 1 > e - 1:
                        dp[b][e] = True

                    else:
                        dp[b][e] = dp[b + 1][e - 1]
                if dp[b][e] == True and end - begin < (e - b):
                    begin, end = b, e
                    # print(begin, end)

        return s[begin : end + 1]
