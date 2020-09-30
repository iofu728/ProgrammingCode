# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 20:19:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 20:20:13

"""
342. Power of Four Easy
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

Accepted 207,506 Submissions 501,423
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xAAAAAAAA == 0

