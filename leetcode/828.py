# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 19:47:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 20:35:36

"""
828. Count Unique Characters of All Substrings of a Given String Hard
Let's define a function countUniqueChars(s) that returns the number of unique characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

On this problem given a string s we need to return the sum of countUniqueChars(t) where t is a substring of s. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.

Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.

## Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

## Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

## Example 3:

Input: s = "LEETCODE"
Output: 92

## Constraints:
0 <= s.length <= 10^4
s contain upper-case English letters only.
Accepted 8,414 Submissions 19,296
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        N, mod, result = len(s), 10 ** 9 + 7, 0
        for ii in range(N):
            jj, kk = ii - 1, ii + 1
            while jj > -1 and s[ii] != s[jj]:
                jj -= 1
            while kk < N and s[ii] != s[kk]:
                kk += 1
            # print((ii - jj) * (kk - ii) % mod, result, ii, jj, kk)
            result += (ii - jj) * (kk - ii) % mod
        return result
