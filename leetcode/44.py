# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-05 00:26:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-05 00:26:58

"""
44. Wildcard Matching Hard
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
Accepted 242,523 Submissions 989,204
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N, M = len(s), len(p)
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True
        for ii in range(1, M + 1):
            if p[ii - 1] == "*":
                dp[0][ii] = True
            else:
                break
        for ii in range(1, N + 1):
            for jj in range(1, M + 1):
                if p[jj - 1] == "*":
                    dp[ii][jj] = dp[ii][jj - 1] or dp[ii - 1][jj]
                elif p[jj - 1] == "?" or s[ii - 1] == p[jj - 1]:
                    dp[ii][jj] = dp[ii - 1][jj - 1]
        return dp[N][M]
