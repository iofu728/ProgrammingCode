# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 14:05:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 14:07:44

"""
461. Hamming Distance Easy
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
Accepted 359,477 Submissions 493,395
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0
        while xor:
            res += 1
            xor = xor & (xor - 1)
        return res
