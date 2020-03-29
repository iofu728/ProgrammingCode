# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 18:45:04
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 18:49:49

"""
1016. Binary String With Substrings Representing 1 To N Medium

Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

## Example 1:
Input: S = "0110", N = 3
Output: true

## Example 2:
Input: S = "0110", N = 4
Output: false

## Note:
1 <= S.length <= 1000
1 <= N <= 10^9

Accepted 12,597 Submissions 21,293
"""


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for ii in range(1, N + 1):
            need = bin(ii).replace("0b", "")
            if need not in S:
                return False
        return True
