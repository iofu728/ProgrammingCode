# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-05 10:49:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-05 12:36:00

"""
1405. Longest Happy String
User Accepted:1684
User Tried:2788
Total Accepted:1733
Total Submissions:5479
Difficulty:Medium
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

## Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

## Example 2:
Input: a = 2, b = 2, c = 1
Output: "aabbc"

## Example 3:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.

## Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        A = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = ""
        for ii in range(a + b + c):
            A.sort(reverse=True)
            for jj in range(3):
                num, t = A[jj]
                if num == 0:
                    continue
                if len(ans) < 2 or not(ans[-1] == ans[-2] == t):
                    ans += t
                    A[jj][0] -= 1
                    break
        return ans
