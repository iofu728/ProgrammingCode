# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 19:56:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 19:57:21

"""
201. Bitwise AND of Numbers Range Medium
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

## Example 1:
Input: [5,7]
Output: 4

## Example 2:
Input: [0,1]
Output: 0

Accepted 97,236 Submissions 261,360
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0
        while n > m:
            res += 1
            m >>= 1
            n >>= 1
        return m << res
