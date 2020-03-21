# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 19:07:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 19:08:23

"""
415. Add Strings Easy

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Accepted
150,785
Submissions
326,449
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        num1, num2 = num1[::-1], num2[::-1]
        max_len = max(len(num1), len(num2))
        num1 = num1 + "0" * (max_len - len(num1))
        num2 = num2 + "0" * (max_len - len(num2))
        remain = 0
        for ii, jj in zip(num1, num2):
            ii = ord(ii) - ord("0")
            jj = ord(jj) - ord("0")
            now = ii + jj + remain
            remain = int(now / 10)
            result.append(str(now % 10))
        if remain != 0:
            result.append(str(remain))
        return "".join(result[::-1])
