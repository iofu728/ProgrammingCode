# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-19 20:35:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-19 20:40:48

"""
466. Count The Repetitions Hard
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
Accepted 9,780 Submissions 35,008
"""


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not n1:
            return 0
        s1num, s2num, idx, recall = 0, 0, 0, {}
        while True:
            s1num += 1
            for c in s1:
                if c != s2[idx]:
                    continue
                idx += 1
                if idx == len(s2):
                    s2num += 1
                    idx = 0
            if s1num == n1:
                return s2num // n2
            if idx in recall:
                s1_t, s2_t = recall[idx]
                pre_t = (s1_t, s2_t)
                in_t = (s1num - s1_t, s2num - s2_t)
                break
            else:
                recall[idx] = (s1num, s2num)
        res = pre_t[1] + (n1 - pre_t[0]) // in_t[0] * in_t[1]
        for ii in range((n1 - pre_t[0]) % in_t[0]):
            for c in s1:
                if c != s2[idx]:
                    continue
                idx += 1
                if idx == len(s2):
                    res += 1
                    idx = 0
        return res // n2
