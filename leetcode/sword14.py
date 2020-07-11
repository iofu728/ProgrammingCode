# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 17:16:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 17:16:50

"""
剑指 Offer 14- II. 剪绳子 II
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：

2 <= n <= 1000
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

通过次数16,681提交次数55,055
"""


class Solution:
    MOD = 10 ** 9 + 7

    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b, x, rem = n // 3 - 1, n % 3, 3, 1
        while a > 0:
            if a % 2:
                rem = (rem * x) % self.MOD
            x = x ** 2 % self.MOD
            a //= 2
        if not b:
            return int(rem * 3) % self.MOD
        if b == 1:
            return int(rem * 4) % self.MOD
        return int(rem * 6) % self.MOD
