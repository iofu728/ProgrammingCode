# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-30 20:42:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-30 21:07:53

"""
面试题62. 圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

## 示例 1：
输入: n = 5, m = 3
输出: 3

## 示例 2：
输入: n = 10, m = 17
输出: 2

## 限制：
1 <= n <= 10^5
1 <= m <= 10^6
通过次数18,860提交次数31,410
"""


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for ii in range(2, n + 1):
            # print(f)
            f = (m + f) % ii
        return f
