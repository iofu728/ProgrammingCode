# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-04-21 10:57:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-04-21 10:57:27

"""
100294. 统计特殊字母的数量 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个字符串 word。如果 word 中同时存在某个字母的小写形式和大写形式，则称这个字母为 特殊字母 。

返回 word 中 特殊字母 的数量。

 

示例 1:

输入：word = "aaAbcBC"

输出：3

解释：

word 中的特殊字母是 'a'、'b' 和 'c'。

示例 2:

输入：word = "abc"

输出：0

解释：

word 中不存在大小写形式同时出现的字母。

示例 3:

输入：word = "abBCab"

输出：1

解释：

word 中唯一的特殊字母是 'b'。

 

提示：

1 <= word.length <= 50
word 仅由小写和大写英文字母组成。
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        for ii in range(26):
            a = chr(ii + ord("a"))
            A = chr(ii + ord("A"))
            if a in word and A in word:
                res += 1
        return res