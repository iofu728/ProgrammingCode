# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-30 11:10:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-30 11:10:16

"""
6222. 美丽整数的最小增量 显示英文描述 
通过的用户数0
尝试过的用户数3
用户总通过次数0
用户总提交次数3
题目难度Medium
给你两个正整数 n 和 target 。

如果某个整数每一位上的数字相加小于或等于 target ，则认为这个整数是一个 美丽整数 。

找出并返回满足 n + x 是 美丽整数 的最小非负整数 x 。生成的输入保证总可以使 n 变成一个美丽整数。

 

示例 1：

输入：n = 16, target = 6
输出：4
解释：最初，n 是 16 ，且其每一位数字的和是 1 + 6 = 7 。在加 4 之后，n 变为 20 且每一位数字的和变成 2 + 0 = 2 。可以证明无法加上一个小于 4 的非负整数使 n 变成一个美丽整数。
示例 2：

输入：n = 467, target = 6
输出：33
解释：最初，n 是 467 ，且其每一位数字的和是 4 + 6 + 7 = 17 。在加 33 之后，n 变为 500 且每一位数字的和变成 5 + 0 + 0 = 5 。可以证明无法加上一个小于 33 的非负整数使 n 变成一个美丽整数。
示例 3：

输入：n = 1, target = 1
输出：0
解释：最初，n 是 1 ，且其每一位数字的和是 1 ，已经小于等于 target 。
 

提示：

1 <= n <= 1012
1 <= target <= 150
生成的输入保证总可以使 n 变成一个美丽整数。
"""
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        @lru_cache(None)
        def get_s(x):
            res = 0
            while x > 0:
                res += x % 10
                x //= 10
            return res
                
        if get_s(n) <= target:
            return 0
        y = 1
        for ii in range(1, 13):
            y *= 10
            m = y - n % y
            if get_s(n + m) <= target:
                return m
            