# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-05 12:49:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-05 12:49:31

"""
100275. K 周期字符串需要的最少操作次数 显示英文描述 
通过的用户数0
尝试过的用户数3
用户总通过次数0
用户总提交次数5
题目难度Medium
给你一个长度为 n 的字符串 word 和一个整数 k ，其中 k 是 n 的因数。

在一次操作中，你可以选择任意两个下标 i 和 j，其中 0 <= i, j < n ，且这两个下标都可以被 k 整除，然后用从 j 开始的长度为 k 的子串替换从 i 开始的长度为 k 的子串。也就是说，将子串 word[i..i + k - 1] 替换为子串 word[j..j + k - 1] 。

返回使 word 成为 K 周期字符串 所需的 最少 操作次数。

如果存在某个长度为 k 的字符串 s，使得 word 可以表示为任意次数连接 s ，则称字符串 word 是 K 周期字符串 。例如，如果 word == "ababab"，那么 word 就是 s = "ab" 时的 2 周期字符串 。

 

示例 1：

输入：word = "leetcodeleet", k = 4

输出：1

解释：可以选择 i = 4 和 j = 0 获得一个 4 周期字符串。这次操作后，word 变为 "leetleetleet" 。

示例 2：

输入：word = "leetcoleet", k = 2

输出：3

解释：可以执行以下操作获得一个 2 周期字符串。

i	j	word
0	2	etetcoleet
4	0	etetetleet
6	0	etetetetet
 

提示：

1 <= n == word.length <= 105
1 <= k <= word.length
k 能整除 word.length 。
word 仅由小写英文字母组成。
"""
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        N = len(word)
        c = Counter([word[ii:ii+k] for ii in range(0, N, k)])
        return N // k - max(c.values())