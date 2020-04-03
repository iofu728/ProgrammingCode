# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 11:51:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 11:52:27

"""
202. Happy Number Easy
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

## Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Accepted 407,146 Submissions 815,066
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        have = {}
        now = sum([int(ii) ** 2 for ii in str(n)])
        while now != 1:
            if now in have:
                return False
            have[now] = True
            now = sum([int(ii) ** 2 for ii in str(now)])
        return True
