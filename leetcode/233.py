# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-02 16:55:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-02 16:56:01

"""
233. Number of Digit One Hard
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
Accepted 48,594 Submissions 155,193
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        res, idx = 0, 1
        while idx <= n:
            tmp = idx * 10
            res += (n // tmp) * idx + min(max(n % tmp - idx + 1, 0), idx)
            idx *= 10
        return res
