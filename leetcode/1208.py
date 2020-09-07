# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 16:30:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-07 16:31:33

"""
1208. Get Equal Substrings Within Budget Medium
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You can't make any change, so the maximum length is 1.
 

Constraints:

1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s and t only contain lower case English letters.
Accepted 16,243 Submissions 38,482
"""
import bisect


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N, M = len(s), len(t)
        need = [abs(ord(ii) - ord(jj)) for ii, jj in zip(s, t)]
        sums, pre = [], 0
        res = 0
        # print(need)
        for right, ii in enumerate(need):

            bisect.insort(sums, pre)
            pre += ii
            left = bisect.bisect_left(sums, pre - maxCost)

            # print(sums, pre)
            # print(left, right, res)
            if right - left + 1 > res:
                res = right - left + 1
        return res

