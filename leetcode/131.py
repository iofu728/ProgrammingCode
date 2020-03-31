# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-31 21:24:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-31 21:57:41

"""
131. Palindrome Partitioning Medium
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

## Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

Accepted 207,775 Submissions 459,529
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        for ii in range(N):
            for jj in range(ii + 1):
                if s[ii] == s[jj] and (ii - jj <= 2 or dp[jj + 1][ii - 1]):
                    dp[jj][ii] = True
        res = []

        def get_palindrome(idx: int, tmp: list):
            if idx == N:
                res.append(tmp)
            for jj in range(idx, N):
                if dp[idx][jj]:
                    get_palindrome(jj + 1, tmp + [s[idx : jj + 1]])

        get_palindrome(0, [])
        return res
