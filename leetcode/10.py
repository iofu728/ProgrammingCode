# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-11 00:26:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-11 00:27:36

"""
10. Regular Expression Matching Hard
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

Accepted 400,682 Submissions 1,521,407
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N, M = len(s), len(p)
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[-1][-1] = True
        for ii in range(N, -1, -1):
            for jj in range(M - 1, -1, -1):
                now = ii < N and p[jj] in {s[ii], "."}
                if jj + 1 < M and p[jj + 1] == "*":
                    dp[ii][jj] = dp[ii][jj + 2] or now and dp[ii + 1][jj]
                else:
                    dp[ii][jj] = now and dp[ii + 1][jj + 1]
        return dp[0][0]
