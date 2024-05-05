# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-05 12:49:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-05 12:49:54

"""
100283. 同位字符串连接的最小长度 显示英文描述 
通过的用户数2
尝试过的用户数3
用户总通过次数2
用户总提交次数3
题目难度Medium
给你一个字符串 s ，它由某个字符串 t 和它的 同位字符串 连接而成。

请你返回字符串 t 的 最小 可能长度。

同位字符串 指的是重新排列一个单词得到的另外一个字符串，原来字符串中的每个字符在新字符串中都恰好只使用一次。

 

示例 1：

输入：s = "abba"

输出：2

解释：

一个可能的字符串 t 为 "ba" 。

示例 2：

输入：s = "cdef"

输出：4

解释：

一个可能的字符串 t 为 "cdef" ，注意 t 可能等于 s 。

 

提示：

1 <= s.length <= 105
s 只包含小写英文字母。
"""
class Solution:
    def minAnagramLength(self, s: str) -> int:
        def is_ok(x):
            if N % x != 0:
                return False
            ref = sorted(s[:x])
            for ii in range(x, N, x):
                if sorted(s[ii: ii + x]) != ref:
                    return False
            return True
        N = len(s)
        for ii in range(1, N + 1):
            if is_ok(ii):
                return ii
