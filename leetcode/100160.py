# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-01-14 15:17:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-01-14 15:17:47

"""
100160. 价值和小于等于 K 的最大数字 显示英文描述 
通过的用户数297
尝试过的用户数915
用户总通过次数362
用户总提交次数2037
题目难度Medium
给你一个整数 k 和一个整数 x 。

令 s 为整数 num 的下标从 1 开始的二进制表示。我们说一个整数 num 的 价值 是满足 i % x == 0 且 s[i] 是 设置位 的 i 的数目。

请你返回 最大 整数 num ，满足从 1 到 num 的所有整数的 价值 和小于等于 k 。

注意：

一个整数二进制表示下 设置位 是值为 1 的数位。
一个整数的二进制表示下标从右到左编号，比方说如果 s == 11100 ，那么 s[4] == 1 且 s[2] == 0 。
 

示例 1：

输入：k = 9, x = 1
输出：6
解释：数字 1 ，2 ，3 ，4 ，5 和 6 二进制表示分别为 "1" ，"10" ，"11" ，"100" ，"101" 和 "110" 。
由于 x 等于 1 ，每个数字的价值分别为所有设置位的数目。
这些数字的所有设置位数目总数是 9 ，所以前 6 个数字的价值和为 9 。
所以答案为 6 。
示例 2：

输入：k = 7, x = 2
输出：9
解释：由于 x 等于 2 ，我们检查每个数字的偶数位。
2 和 3 在二进制表示下的第二个数位为设置位，所以它们的价值和为 2 。
6 和 7 在二进制表示下的第二个数位为设置位，所以它们的价值和为 2 。
8 和 9 在二进制表示下的第四个数位为设置位但第二个数位不是设置位，所以它们的价值和为 2 。
数字 1 ，4 和 5 在二进制下偶数位都不是设置位，所以它们的价值和为 0 。
10 在二进制表示下的第二个数位和第四个数位都是设置位，所以它的价值为 2 。
前 9 个数字的价值和为 6 。
前 10 个数字的价值和为 8，超过了 k = 7 ，所以答案为 9 。
 

提示：

1 <= k <= 1015
1 <= x <= 8
"""
"""

1. 二分+数位DP  3404ms

给定 num，统计 1~num 的价值和，判断价值和是否 <= k
二分相当于多花费 log 的时间，额外增加一个条件

2. 二分+枚举数位

"""
class Solution:
    def countDigitOne(self, num: int, x: int) -> int:
        res = 0
        shift = x - 1
        n = num >> shift
        while n:
            # 第一部分
            res += (n // 2) << shift
            # 第二部分
            if n % 2:
                mask = (1 << shift) - 1
                res += (num & mask) + 1
            shift += x
            n >>= x
        return res
        

        # s = bin(n)[2:]
        # m = len(s)
        # O(m^2)
        # @cache
        # def f(i: int, cnt1: int, is_limit: bool) -> int:
        #     if i == len(s):
        #         return cnt1
        #     res = 0
        #     up = int(s[i]) if is_limit else 1
        #     for d in range(up + 1):  # 枚举要填入的数字 d
        #         res += f(i + 1, cnt1 + (d == 1 and (len(s)-i)%x == 0), is_limit and d == up)
        #     return res
        # return f(0, 0, True)

    def findMaximumNumber(self, k: int, x: int) -> int:
        left = 0  # self.countDigitOne(left) <= k
        right = (k + 1) << x  # self.countDigitOne(right) > k
        while left + 1 < right:
            mid = (left + right) // 2
            if self.countDigitOne(mid, x) <= k:
                left = mid
            else:
                right = mid
        return left
