# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-15 18:49:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-15 18:49:40

"""
29. Divide Two Integers Medium
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
Accepted 256,365 Submissions 1,582,831
"""


class Solution:
    def divide(self, A: int, B: int) -> int:
        flag = (A > 0) ^ (B > 0)
        A, B, c, res = abs(A), abs(B), 0, 0
        while A >= B:
            c += 1
            B <<= 1
        for ii in range(c - 1, -1, -1):
            B >>= 1
            if A >= B:
                res += 1 << ii
                A -= B
        if flag:
            res = -res
        return res if -(1 << 31) <= res <= (1 << 31) - 1 else (1 << 31) - 1
