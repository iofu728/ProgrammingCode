# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-06 21:45:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-06 21:45:29

"""
424. Longest Repeating Character Replacement
Medium

3169

130

Add to List

Share
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
Accepted
144,185
Submissions
290,431
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dp = defaultdict(int)
        res, left, right = 0, 0, 0
        while right < len(s):
            dp[s[right]] += 1
            res = max(res, dp[s[right]])
            if right - left + 1 - res > k:
                dp[s[left]] -= 1
                left += 1
            right += 1
        return right - left
