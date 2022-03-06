# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-03 20:36:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-03 20:36:57

"""
1653. Minimum Deletions to Make String Balanced
Medium

604

16

Add to List

Share
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
Accepted
16,163
Submissions
29,349
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        d = [0] * (N + 1)
        for ii in range(N - 1, -1, -1):
            d[ii] = d[ii + 1] + int(s[ii] == "a")
        res, pre = 10 ** 9 + 7, 0
        for jj, ii in enumerate(s):
            if ii == "a":
                continue
            res = min(res, d[jj] + pre)
            pre += ii == "b"
        c = s.count("a")
        res = min(res, c, N - c)
        return res if res != 10 ** 9 + 7 else 0