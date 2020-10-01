# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-01 19:10:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-01 19:11:20

"""
264. Ugly Number II Medium
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
Accepted 186,594 Submissions 441,240
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res, have = [1], [2, 3, 5]
        i2, i3, i5 = 0, 0, 0
        for ii in range(1, n + 1):
            tmp = min(res[i2] * 2, res[i3] * 3, res[i5] * 5)
            if tmp == res[i2] * 2:
                i2 += 1
            if tmp == res[i3] * 3:
                i3 += 1
            if tmp == res[i5] * 5:
                i5 += 1
            res.append(tmp)
        # print(res)
        return res[n - 1]

