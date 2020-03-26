# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-26 20:53:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-26 22:17:12

"""
76. Minimum Window Substring Hard

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

## Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

## Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
Accepted 345,875 Submissions 1,031,260
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        NEED_MAP = Counter(t)
        have, need = {}, {k: v for k, v in NEED_MAP.items()}
        left, right = 0, 0
        N, M = len(s), len(t)
        min_substr, min_len = "", 0x3FFFFFFF
        while left <= right and left < N and right < N:
            while len(need) and right < N:
                t = s[right]
                have[t] = have.get(t, 0) + 1
                if t in need:
                    need[t] -= 1
                    if need[t] == 0:
                        del need[t]
                right += 1
            if not len(need) and right - left < min_len:
                min_substr = s[left:right]
                min_len = len(min_substr)
            # print(min_substr, min_len, s[left: right], left, right, need, have)
            while not len(need) and left <= right and left < N:
                t = s[left]
                have[t] -= 1
                if t in NEED_MAP and have[t] < NEED_MAP[t]:
                    need[t] = need.get(t, 0) + 1
                left += 1
            t = max(left - 1, 0)
            tt = Counter(list(s[t:right]))
            yy = {k: 1 for k, v in NEED_MAP.items() if (not k in tt) or tt[k] < v}
            if len(need) == 1 and len(yy) == 0 and right - t < min_len:
                min_substr = s[t:right]
                min_len = len(min_substr)
            # print(min_substr, min_len, s[t:right], t, left, right, yy, need, have)
        return min_substr
