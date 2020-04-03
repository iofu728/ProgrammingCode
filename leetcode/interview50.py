# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 11:34:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 11:34:35

"""
面试题50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "

## 限制：
0 <= s 的长度 <= 50000

通过次数8,681提交次数14,625
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        single = {}
        for ii in s:
            single[ii] = not ii in single
        for ii in s:
            if single[ii]:
                return ii
        return " "
