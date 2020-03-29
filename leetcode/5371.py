# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 11:01:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 12:01:34

"""
5371. Find All Good Strings
User Accepted:75
User Tried:544
Total Accepted:79
Total Submissions:1072
Difficulty:Hard
Given the strings s1 and s2 of size n, and the string evil. Return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:

Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 
Example 2:

Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.
Example 3:

Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2
 

Constraints:

s1.length == n
s2.length == n
1 <= n <= 500
1 <= evil.length <= 50
All strings consist of lowercase English letters.
"""


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        N, A, mod = len(s1), 26, 2 ** 32

        def get_prefix(a: str, b: str):
            result = ""
            for ii in range(min(len(a), len(b))):
                if a[ii] == b[ii]:
                    result += a[ii]
                else:
                    return result
            return result

        def get_num(a: str):
            result = 0
            for ii in a:
                result = (result * A + ord(ii) - ord("a")) % mod
            return result

        def get_common(a: str, b: str):
            result = ""
            for ii in range(1, len(b) + 1):
                # print(result, a[-ii:], b[:ii])
                if a[-ii:] == b[:ii]:
                    result = b[ii:]

            return result

        prefix = get_prefix(s1, s2)
        if evil in prefix:
            return 0

        N_re = N - len(prefix)
        s1_re, s2_re = s1[-N_re:], s2[-N_re:]
        a_num = get_num(s1_re)
        b_num = get_num(s2_re)
        t_num = get_num(evil)
        # remove_num = (int(b_num / t_num) - int(a_num / t_num)) / A
        L = [A ** ii for ii in range(N_re)]
        remove_num = 0
        tt = get_common(prefix, evil)
        tt_num = get_num(tt) if tt != "" else 0
        # print(prefix, tt, tt_num)
        for ii in range(a_num, b_num + 1):
            # if tt != "" and int(ii / L[-1]) == tt_num:
            #     remove_num += 1
            #     continue
            for jj in L:
                if int(ii / jj) == t_num or ii % jj == t_num:
                    # print(ii, jj)
                    remove_num += 1
                    break
        # print(a_num, b_num, t_num, remove_num, L)
        return b_num - a_num + 1 - remove_num
