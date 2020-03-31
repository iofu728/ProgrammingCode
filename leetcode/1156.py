# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-30 22:38:18
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-30 22:39:31

"""
1156. Swap For Longest Repeated Character Substring Medium
Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

## Example 1:
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.

## Example 2:
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.

## Example 3:
Input: text = "aaabbaaa"
Output: 4

## Example 4:
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.

## Example 5:
Input: text = "abcdef"
Output: 1

## Constraints:
1 <= text.length <= 20000
text consist of lowercase English characters only.

Accepted 7,165 Submissions 15,035
"""
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        N = len(text)
        if not N:
            return 0
        left, right, c, ans = [1] * N, [1] * N, 1, 1
        count = Counter(text)
        for ii in range(1, N):
            c = 1 if text[ii] != text[ii - 1] else c + 1
            left[ii] = c
        c = 1
        for ii in range(N - 2, -1, -1):
            c = 1 if text[ii] != text[ii + 1] else c + 1
            right[ii] = c
        ans = max(max(left), max(right))
        for ii in range(1, N - 1):
            if count[text[ii - 1]] > left[ii - 1]:
                ans = max(ans, left[ii - 1] + 1)
            if count[text[ii + 1]] > right[ii + 1]:
                ans = max(ans, right[ii + 1] + 1)
            if text[ii - 1] == text[ii + 1] and text[ii] != text[ii - 1]:
                if count[text[ii - 1]] > left[ii - 1] + right[ii + 1]:
                    ans = max(ans, left[ii - 1] + right[ii + 1] + 1)
                else:
                    ans = max(ans, left[ii - 1] + right[ii + 1])
        return ans
