# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-26 22:02:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-26 22:03:34

"""
316. Remove Duplicate Letters Hard
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Accepted 81,663 Submissions 227,107
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        pos, N = 0, len(s)
        for ii in range(N):
            if s[ii] < s[pos]:
                pos = ii
            c[s[ii]] -= 1
            if c[s[ii]] == 0:
                break
        # print(s[pos])
        return (
            s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], ""))
            if s
            else ""
        )

