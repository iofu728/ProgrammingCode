# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-03-17 12:28:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-03-17 12:28:51

"""
100236. 统计以给定字符开头和结尾的子字符串总数 显示英文描述 
通过的用户数8
尝试过的用户数12
用户总通过次数8
用户总提交次数12
题目难度Medium
给你一个字符串 s 和一个字符 c 。返回在字符串 s 中并且以 c 字符开头和结尾的非空子字符串的总数。

 

示例 1：

输入：s = "abada", c = "a"

输出：6

解释：以 "a" 开头和结尾的子字符串有： "abada"、"abada"、"abada"、"abada"、"abada"、"abada"。

示例 2：

输入：s = "zzz", c = "z"

输出：6

解释：字符串 s 中总共有 6 个子字符串，并且它们都以 "z" 开头和结尾。

 

提示：

1 <= s.length <= 105
s 和 c 均由小写英文字母组成。

"""
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        d = 0
        for ii in s:
            if ii == c:
                d += 1
        return d * (d + 1) // 2