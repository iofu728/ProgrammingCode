# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-10-20 12:35:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-10-20 12:35:47

"""
100369. Count Substrings With K-Frequency Characters I
User Accepted:114
User Tried:152
Total Accepted:117
Total Submissions:169
Difficulty:Medium
Given a string s and an integer k, return the total number of substrings of s where at least one character appears at least k times.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "abacb", k = 2

Output: 4

Explanation:

The valid substrings are:

"aba" (character 'a' appears 2 times).
"abac" (character 'a' appears 2 times).
"abacb" (character 'a' appears 2 times).
"bacb" (character 'b' appears 2 times).
Example 2:

Input: s = "abcde", k = 1

Output: 15

Explanation:

All substrings are valid because every character appears at least once.

 

Constraints:

1 <= s.length <= 3000
1 <= k <= s.length
s consists only of lowercase English letters.
"""

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        res = 0
        for x in range(N):
            c = defaultdict(int)
            r = x
            while r < N:
                c[s[r]] += 1
                if c[s[r]] == k:
                    res += N - r
                    break
                r += 1
        return res
        