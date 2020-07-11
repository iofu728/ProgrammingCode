# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 15:07:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 15:08:17

"""
面试题 01.05. 一次编辑
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True

示例 2:

输入: 
first = "pales"
second = "pal"
输出: False
通过次数9,021提交次数27,885
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        N, M = len(first), len(second)
        NN, MM = min(N, M), max(N, M)
        if MM - NN > 1:
            return False
        left, right = 0, 0
        while left < NN and first[left] == second[left]:
            left += 1
        while right < NN and first[-right - 1] == second[-right - 1]:
            right += 1
        # print(left, right, MM, NN)
        return left + right >= NN or (MM == NN and left + right + 1 == NN)
