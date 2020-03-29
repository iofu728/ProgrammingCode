# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-29 22:06:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-29 22:11:12

"""
1190. Reverse Substrings Between Each Pair of Parentheses Medium
You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

## Example 1:

Input: s = "(abcd)"
Output: "dcba"

## Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

## Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

## Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"

## Constraints:
0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
Accepted 12,878 Submissions 21,543
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        N, res, stack = len(s), "", []
        for c in s:
            if c == "(":
                stack.append(res)
                res = ""
            elif c == ")":
                res = res[::-1]
                res = stack[-1] + res
                stack = stack[:-1]
            else:
                res += c
        return res
