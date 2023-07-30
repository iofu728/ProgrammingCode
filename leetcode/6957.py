# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-07-30 12:36:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-07-30 12:37:07

"""
6957. 统计范围内的步进数字数目 显示英文描述 
通过的用户数124
尝试过的用户数210
用户总通过次数139
用户总提交次数425
题目难度Hard
给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。

如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。

请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。

由于答案可能很大，请你将它对 109 + 7 取余 后返回。

注意：步进数字不能有前导 0 。

 

示例 1：

输入：low = "1", high = "11"
输出：10
解释：区间 [1,11] 内的步进数字为 1 ，2 ，3 ，4 ，5 ，6 ，7 ，8 ，9 和 10 。总共有 10 个步进数字。所以输出为 10 。
示例 2：

输入：low = "90", high = "101"
输出：2
解释：区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。
 

提示：

1 <= int(low) <= int(high) < 10100
1 <= low.length, high.length <= 100
low 和 high 只包含数字。
low 和 high 都不含前导 0 。
"""
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        mod = 1000000007

        def f(s: str) -> int:
            a = [0] * 20
            h = True
            for c in s:
                d = ord(c) - ord("0")
                b = [0] * 20
                for j in range(1, 10):
                    if j <= d or not h:
                        b[(j < d or not h) * 10 + j] += 1
                for i in range(20):
                    x = i // 10
                    y = i % 10
                    for j in range(10):
                        if abs(y - j) != 1:
                            continue
                        if j > d and not x:
                            continue
                        nx = x or j < d
                        b[nx * 10 + j] += a[i]
                a = [bi % mod for bi in b]
                h = False
            return sum(a)

        return (f(high) - f(str(int(low) - 1))) % mod