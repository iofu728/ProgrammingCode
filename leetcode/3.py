# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 13:51:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 13:52:46

"""
3. Longest Substring Without Repeating Characters Medium
Given a string, find the length of the longest substring without repeating characters.

## Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

## Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

## Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Accepted 1,398,099 Submissions 4,702,679
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def is_ok(a: dict):
            for k, v in a.items():
                if not v in [0, 1]:
                    return False
            return True

        N, left, right, have, res = len(s), 0, 0, {}, 0
        while left <= right and right < N and left >= 0:
            tl, tr = left, right
            while is_ok(have) and right < N:
                have[s[right]] = have.get(s[right], 0) + 1
                right += 1
            if right - left - 1 > res:
                res = right - left - 1
            while not is_ok(have) and left < right:
                have[s[left]] -= 1
                left += 1
            if right - left > res:
                res = right - left
            # print(left, right, tl, tr)
        return res
