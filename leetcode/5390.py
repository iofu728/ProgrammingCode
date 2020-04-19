# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-19 10:48:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-19 11:15:37

"""
5390. Minimum Number of Frogs Croaking
User Accepted:1049
User Tried:1544
Total Accepted:1054
Total Submissions:2341
Difficulty:Medium
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1
 

Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
"""
from collections import Counter


class Solution:
    def minNumberOfFrogs(self, s: str) -> int:
        # s = s.replace("croak", "")
        if len(s) == 0:
            return 1
        count = Counter(s)
        if len(count) != 5 or len(set(count.values())) != 1:
            return -1
        c, r, o, a, k = [], [], [], [], []
        for ii, jj in enumerate(s):
            if jj == "c":
                c.append(ii)
            elif jj == "r":
                r.append(ii)
            elif jj == "o":
                o.append(ii)
            elif jj == "a":
                a.append(ii)
            elif jj == "k":
                k.append(ii)
        for ii, jj, kk, mm, nn in zip(c, r, o, a, k):
            if not (ii < jj < kk < mm < nn):
                return -1
        # print(c, r, o, a, k)
        res, max_num = [], 0
        for ii, jj in zip(c, k):
            if not len(res):
                res.append(jj)
                continue
            pre_j = res[0]
            if pre_j > ii:
                res.append(jj)
            else:
                res = res[1:]
                res.append(jj)
        return len(res)
