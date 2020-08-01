# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-28 22:42:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-28 22:45:02

"""
1006. Clumsy Factorial Medium
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.

Example 1:

Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1
Example 2:

Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

Note:

1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)
Accepted 12,603 Submissions 23,609
"""


class Solution:
    def clumsy(self, N: int) -> int:
        def once(a: list):
            res = 0
            for ii, jj in enumerate(a):
                if ii == 0:
                    res = -jj
                    if jj == N:
                        res *= -1
                elif ii == 1:
                    res *= jj
                elif ii == 2:
                    tmp = res
                    res //= jj
                    if tmp % jj != 0 and tmp < 0:
                        res += 1
                else:
                    res += jj
            # print(a, res)
            return res

        res = 0
        for ii in range(N, 0, -4):
            res += once(range(ii, max(ii - 4, 0), -1))
        return res

