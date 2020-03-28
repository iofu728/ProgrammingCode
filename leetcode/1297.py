# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-28 21:15:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-28 22:04:58

"""
1297. Maximum Number of Occurrences of a Substring Medium
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.

## Example 1:
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

## Example 2:
Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

## Example 3:
Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3

## Example 4:
Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0

## Constraints:
1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.
Accepted 6,528 Submissions 14,604
"""
from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        N, L, have = len(s), minSize, {}
        before, max_num, max_str = s[:L], 0, ""
        count = Counter(before)
        if len(count) <= maxLetters:
            have[before] = 1
            max_num, max_str = 1, before
        for b in range(1, N - L + 1):
            e = b + L - 1
            now = before[1:] + s[e]
            count[s[b - 1]] -= 1
            count[s[e]] = count.get(s[e], 0) + 1
            if count[s[b - 1]] == 0:
                del count[s[b - 1]]
            # print(b, e, have, count)
            if len(count) <= maxLetters:
                have[now] = have.get(now, 0) + 1
                if have[now] > max_num:
                    max_num = have[now]
                    max_str = now
            before = now
        # print(have, count)
        return max_num
