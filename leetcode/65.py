# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-06-17 19:54:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-17 19:54:47

"""
65. Valid Number Hard
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
Accepted 219,515 Submissions 1,313,973
"""
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        if s[0] in "+-":
            s = s[1:]
        s = s.lower()
        if re.findall("[a-df-z]", s) or s.count(".") > 1 or s.count("e") > 1:
            return False
        if "e" in s:
            num, index = s.split("e")
            if index and index[0] in "+-":
                index = index[1:]
        else:
            num, index = s, "1"
        if "." in num:
            a, b = num.split(".")
            if not (not a or (a and a.isdigit())):
                return False
            if not (not b or (b and b.isdigit())):
                return False
            if not a and not b:
                return False
        else:
            if not (num and num.isdigit()):
                return False
        if not (index and index.isdigit()):
            return False
        return True