# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-28 00:45:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-28 01:07:01

"""
647. Palindromic Substrings Medium
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

## Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

## Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

## Note:
The input string length won't exceed 1000.

Accepted 156,842 Submissions 263,852
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        result = []
        for ii in range(N):
            dp[ii][ii] = True
            result.append(s[ii : ii + 1])

        for jj in range(2, N + 1):
            for b in range(N - jj + 1):
                e = b + jj - 1
                # print(b, e)
                if s[b] == s[e]:
                    if b + 1 > e - 1:
                        dp[b][e] = True
                    else:
                        dp[b][e] = dp[b + 1][e - 1]
                if dp[b][e] == True:
                    result.append(s[b : e + 1])
        # print(dp)
        # print(result)
        return len(result)
