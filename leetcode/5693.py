# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-03-20 22:32:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-03-20 22:32:17

'''
5693. 字符串中第二大的数字 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。

混合字符串 由小写英文字母和数字组成。

 

示例 1：

输入：s = "dfa12321afd"
输出：2
解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
示例 2：

输入：s = "abc1111"
输出：-1
解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
 

提示：

1 <= s.length <= 500
s 只包含小写英文字母和（或）数字。
'''

class Solution:
    def secondHighest(self, s: str) -> int:
        a, b = -1, -1
        for ii in s:
            if not ii.isdigit():
                continue
            c = int(ii)
            if c > a:
                a, b = c, a
            elif b < c < a:
                b = c
        return b