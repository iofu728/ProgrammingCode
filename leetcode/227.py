# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-28 18:09:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-28 18:10:05

"""
227. Basic Calculator II Medium
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
Accepted 193,643 Submissions 522,989
"""
import re


class Solution:
    def calculate(self, s: str) -> int:
        s = re.sub("([*+-/])", r" \1 ", s.replace(" ", "")).split()
        (first, *nums), ops = s[::2], s[1::2]
        queue, signs = [int(first)], []
        for ii, jj in zip(nums, ops):
            if jj == "*":
                queue[-1] *= int(ii)
            elif jj == "/":
                queue[-1] //= int(ii)
            else:
                queue.append(int(ii))
                signs.append(1 if jj == "+" else -1)
        return queue[0] + sum([ii * jj for ii, jj in zip(queue[1:], signs)])
