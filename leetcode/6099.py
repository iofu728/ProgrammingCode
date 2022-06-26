# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-06-19 12:17:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-06-19 12:17:39
"""
6099. 小于等于 K 的最长二进制子序列 显示英文描述 
通过的用户数2
尝试过的用户数2
用户总通过次数2
用户总提交次数2
题目难度Medium
给你一个二进制字符串 s 和一个正整数 k 。

请你返回 s 的 最长 子序列，且该子序列对应的 二进制 数字小于等于 k 。

注意：

子序列可以有 前导 0 。
空字符串视为 0 。
子序列 是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。
 

示例 1：

输入：s = "1001010", k = 5
输出：5
解释：s 中小于等于 5 的最长子序列是 "00010" ，对应的十进制数字是 2 。
注意 "00100" 和 "00101" 也是可行的最长子序列，十进制分别对应 4 和 5 。
最长子序列的长度为 5 ，所以返回 5 。
示例 2：

输入：s = "00101001", k = 1
输出：6
解释："000001" 是 s 中小于等于 1 的最长子序列，对应的十进制数字是 1 。
最长子序列的长度为 6 ，所以返回 6 。
 

提示：

1 <= s.length <= 1000
s[i] 要么是 '0' ，要么是 '1' 。
1 <= k <= 109
"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        pre = 0
        N = len(s)
        x = int(s, 2)
        y = pow(2, N - 1)
        for ii in range(N):
            if x <= k:
                # print(pre, N - ii)
                res = max(res, pre + N - ii)
            if s[ii] == "0":
                pre += 1
            x -= y * (int(s[ii]))
            y //= 2
        return res
