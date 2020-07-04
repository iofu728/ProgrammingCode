# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-04 23:26:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-04 23:26:46

"""
32. Longest Valid Parentheses Hard
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
Accepted 282,662 Submissions 1,005,192
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        dp = [0] * N
        for ii in range(1, N):
            if s[ii] == "(":
                continue
            if s[ii - 1] == "(":
                dp[ii] = (dp[ii - 2] if ii >= 2 else 0) + 2
            elif ii - dp[ii - 1] > 0 and s[ii - 1 - dp[ii - 1]] == "(":
                dp[ii] = (
                    dp[ii - 1]
                    + (dp[ii - 2 - dp[ii - 1]] if ii - dp[ii - 1] >= 2 else 0)
                    + 2
                )
        # print(dp)
        return max(dp) if N else 0
