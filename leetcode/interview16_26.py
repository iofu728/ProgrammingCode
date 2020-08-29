# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-28 16:46:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-28 16:51:16

"""
面试题 16.26. 计算器
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
"""
import re


class Solution:
    def calculate(self, s: str) -> int:
        s = re.sub("([*+-/])", r" \1 ", s.replace(" ", "")).split()
        (first, *nums), op = s[::2], s[1::2]
        queue, signs = [int(first)], []
        for o, num in zip(op, nums):
            if o == "*":
                queue[-1] *= int(num)
            elif o == "/":
                queue[-1] //= int(num)
            else:
                queue.append(int(num))
                signs.append(1 if o == "+" else -1)
        return queue[0] + sum([ii * jj for ii, jj in zip(queue[1:], signs)])
