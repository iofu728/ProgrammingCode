# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 19:21:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 19:21:54

"""
43. Multiply Strings Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Accepted 263,432 Submissions 803,314
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for ii in num1:
            remain, tmp = 0, 0
            ii = ord(ii) - ord("0")
            for jj in num2:
                jj = ord(jj) - ord("0")
                now = ii * jj
                tmp = tmp * 10 + now
            result = result * 10 + tmp
        return str(result)
