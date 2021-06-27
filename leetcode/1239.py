# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-06-19 14:16:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-19 14:17:32

"""
1239. Maximum Length of a Concatenated String with Unique Characters Medium
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
Accepted 63,835 Submissions 126,479
"""
from collections import Counter


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N, self.res = len(arr), 0

        def dfs(c: dict, idx: int):
            v = set(c.values())
            if self.res == 26:
                return
            # print(c, v, idx)
            if v != set() and v != set([1]):
                return
            self.res = max(self.res, len(c))
            if idx >= N:
                return
            dfs(c, idx + 1)
            for k in arr[idx]:
                c[k] += 1
            dfs(c, idx + 1)
            for k in arr[idx]:
                c[k] -= 1
                if c[k] == 0:
                    del c[k]

        dfs(Counter(), 0)
        return self.res