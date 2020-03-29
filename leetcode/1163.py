# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 20:44:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 21:41:15

"""
1163. Last Substring in Lexicographical Order Hard

Given a string s, return the last substring of s in lexicographical order.

## Example 1: 
Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

## Example 2:
Input: "leetcode"
Output: "tcode"

## Note:
1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.

Accepted 9,417 Submissions 28,688
"""


class Solution:
    def lastSubstring(self, s: str) -> str:
        N, MAX = len(s), 100000
        if not N:
            return ""
        have, max_alpha = {}, "a"
        for ii, jj in enumerate(s):
            if ii > 0 and jj <= s[ii - 1]:
                continue
            if jj not in have:
                t = ii
            else:
                t = max([ii, have[jj]], key=lambda i: (s[i : i + MAX], -i))
            have[jj] = t
            t = ord(jj) - ord("a")
            if t > ord(max_alpha) - ord("a"):
                max_alpha = jj
        # nums = sorted(have[max_alpha], key=lambda i:s[i:])
        return s[have[max_alpha] :]
