# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-07-07 11:47:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-07-07 11:47:35

"""
100339. 找出加密后的字符串 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个字符串 s 和一个整数 k。请你使用以下算法加密字符串：

对于字符串 s 中的每个字符 c，用字符串中 c 后面的第 k 个字符替换 c（以循环方式）。
返回加密后的字符串。

 

示例 1：

输入： s = "dart", k = 3

输出： "tdar"

解释：

对于 i = 0，'d' 后面的第 3 个字符是 't'。
对于 i = 1，'a' 后面的第 3 个字符是 'd'。
对于 i = 2，'r' 后面的第 3 个字符是 'a'。
对于 i = 3，'t' 后面的第 3 个字符是 'r'。
示例 2：

输入： s = "aaa", k = 1

输出： "aaa"

解释：

由于所有字符都相同，加密后的字符串也将相同。

 

提示：

1 <= s.length <= 100
1 <= k <= 104
s 仅由小写英文字母组成。
"""
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        N = len(s)
        res = ""
        for ii in range(N):
            n_idx = (ii + k) % N
            res += s[n_idx]
        return res