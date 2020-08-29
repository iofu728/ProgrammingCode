# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 22:58:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 22:59:27

"""
537. Complex Number Multiplication Medium
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
Accepted 48,301 Submissions 71,614
"""


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        ax, ay = [int(ii) for ii in a[:-1].split("+")]
        bx, by = [int(ii) for ii in b[:-1].split("+")]
        cx = ax * bx - ay * by
        cy = ax * by + ay * bx
        return "{}+{}i".format(cx, cy)
