# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 14:44:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 14:44:49

"""
459. Repeated Substring Pattern Easy
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
Accepted 132,053 Submissions 313,111
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(query: str, pattern: str) -> bool:
            N, M = len(query), len(pattern)
            pmt = [-1] * M
            for ii in range(1, M):
                jj = pmt[ii - 1]
                while jj != -1 and pattern[jj + 1] != pattern[ii]:
                    jj = pmt[jj]
                if pattern[jj + 1] == pattern[ii]:
                    pmt[ii] = jj + 1
            match = -1
            for ii in range(1, N - 1):
                while match != -1 and query[ii] != pattern[match + 1]:
                    match = pmt[match]
                if pattern[match + 1] == query[ii]:
                    match += 1
                    if match == M - 1:
                        return True
            return False

        return kmp(s + s, s)
