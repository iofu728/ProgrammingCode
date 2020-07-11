# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 16:48:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 16:49:18

"""
343. Integer Break Medium
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.

Accepted 107,105 Submissions 213,878
"""
from math import pow


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if not b:
            return int(pow(3, a))
        if b == 1:
            return int(pow(3, a - 1) * 4)
        return int(pow(3, a) * 2)
