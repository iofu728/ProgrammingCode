# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-23 23:20:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-23 23:22:00

"""
678. Valid Parenthesis String Medium
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
Accepted 120,056 Submissions 384,078
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        x, y = 0, 0
        for ii in s:
            if ii == "(":
                x += 1
                y += 1
            elif ii == ")":
                if x > 0:
                    x -= 1
                y -= 1
            else:
                if x > 0:
                    x -= 1
                y += 1
            if y < 0:
                return False
        return x == 0
