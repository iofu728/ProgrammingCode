# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-04-21 10:57:45
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-04-21 10:57:55

"""
100291. 统计特殊字母的数量 II 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个字符串 word。如果 word 中同时出现某个字母 c 的小写形式和大写形式，并且 每个 小写形式的 c 都出现在第一个大写形式的 c 之前，则称字母 c 是一个 特殊字母 。

返回 word 中 特殊字母 的数量。

 

示例 1:

输入：word = "aaAbcBC"

输出：3

解释：

特殊字母是 'a'、'b' 和 'c'。

示例 2:

输入：word = "abc"

输出：0

解释：

word 中不存在特殊字母。

示例 3:

输入：word = "AbBCab"

输出：0

解释：

word 中不存在特殊字母。

 

提示：

1 <= word.length <= 2 * 105
word 仅由小写和大写英文字母组成。
"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c1, c2 = defaultdict(int), defaultdict(int)
        N = len(word)
        for ii in range(N):
            if word[ii].islower():
                c1[word[ii]] = ii
            elif word[ii] not in c2:
                c2[word[ii]] = ii
        res = 0
        for ii in range(26):
            a = chr(ii + ord("a"))
            A = chr(ii + ord("A"))
            if a in c1 and A in c2 and c1[a] < c2[A]:
                res += 1
        return res
                