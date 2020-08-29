# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 12:26:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 12:27:34


"""
214. Shortest Palindrome Hard
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
Accepted 100,920 Submissions 337,750
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        pmt = [-1] * N
        for ii in range(1, N):
            jj = pmt[ii - 1]
            while jj != -1 and s[jj + 1] != s[ii]:
                # print(jj, pmt[jj], s[jj + 1], s[ii])
                jj = pmt[jj]
            if s[jj + 1] == s[ii]:
                pmt[ii] = jj + 1
            print(ii, jj, s[jj + 1], s[ii], pmt[ii])
        # print(pmt)
        best = -1
        for ii in range(N - 1, -1, -1):
            # print(best)
            while best != -1 and s[best + 1] != s[ii]:
                best = pmt[best]
            if s[best + 1] == s[ii]:
                best += 1
        # print(best)
        add = "" if best == N - 1 else s[best + 1 :]
        return add[::-1] + s
