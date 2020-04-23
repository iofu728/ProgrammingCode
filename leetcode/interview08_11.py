# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-23 20:20:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-23 20:20:31

"""
面试题 08.11. Coin LCCI
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents. (The result may be large, so you should return it modulo 1000000007)

Example1:

 Input: n = 5
 Output: 2
 Explanation: There are two ways:
5=5
5=1+1+1+1+1
Example2:

 Input: n = 10
 Output: 4
 Explanation: There are four ways:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
Notes:

You can assume:

0 <= n <= 1000000
通过次数10,869提交次数21,529
"""


class Solution:
    MOD = 10 ** 9 + 7

    def waysToChange(self, n: int) -> int:
        res = 0
        for ii in range(n // 25 + 1):
            r = n - ii * 25
            a, b = r // 10, r % 10 // 5
            res += (a + 1) * (a + b + 1)
        return res % self.MOD
