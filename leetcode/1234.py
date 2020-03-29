# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 18:50:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 19:31:26

"""
1234. Replace the Substring for Balanced String Medium

You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.

## Example 1:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

## Example 2:
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

## Example 3:
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 

## Example 4:
Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".

## Constraints:

1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.

Accepted 7,546 Submissions 24,026
"""
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        def a_in_b(a: dict, b: dict) -> bool:
            for k, v in a.items():
                if k not in b:
                    return False
                if v > b[k]:
                    return False
            return True

        N = len(s)
        need = int(N // 4)
        result = []
        for k, v in Counter(s).items():
            if v > need:
                result.extend([k] * (v - need))
        if not len(result):
            return 0
        left, right, min_num = 0, len(result), 9999999
        need_str = Counter(result)
        have = Counter(s[:right])
        if a_in_b(need_str, have):
            return right
        while left < right and right < N and left >= 0:
            # print(left, right)
            t = left
            while not a_in_b(need_str, have) and right < N:
                have[s[right]] = have.get(s[right], 0) + 1
                right += 1
            while a_in_b(need_str, have) and left < N:
                have[s[left]] -= 1
                left += 1
            # if t != left
            t = left - 1 if t != left else t
            have[s[t]] += 1
            if a_in_b(need_str, have):
                if min_num > right - t:
                    # print(t, right, need_str, have)
                    min_num = right - t
            have[s[t]] -= 1

        # print(have, min_num)
        return min_num
