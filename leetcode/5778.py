# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-06-06 12:31:49
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-06 12:32:00
"""
5778. 使二进制字符串字符交替的最少反转次数 显示英文描述 
通过的用户数13
尝试过的用户数30
用户总通过次数13
用户总提交次数36
题目难度Medium
给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次：

类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。
类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。
请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。

我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。

比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。
 

示例 1：

输入：s = "111000"
输出：2
解释：执行第一种操作两次，得到 s = "100011" 。
然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
示例 2：

输入：s = "010"
输出：0
解释：字符串已经是交替的。
示例 3：

输入：s = "1110"
输出：1
解释：对第二个字符执行第二种操作，得到 s = "1010" 。
 

提示：

1 <= s.length <= 105
s[i] 要么是 '0' ，要么是 '1' 。
"""


class Solution:
    def minFlips(self, s: str) -> int:
        N = len(s)
        a = len(
            [1 for ii in range(N // 2 + 1) if 2 * ii < N and s[2 * ii] == "1"]
        ) + len(
            [1 for ii in range(N // 2 + 1) if 2 * ii + 1 < N and s[2 * ii + 1] == "0"]
        )
        b = len(
            [1 for ii in range(N // 2 + 1) if 2 * ii < N and s[2 * ii] == "0"]
        ) + len(
            [1 for ii in range(N // 2 + 1) if 2 * ii + 1 < N and s[2 * ii + 1] == "1"]
        )
        dp = [a, b]
        res = min(a, b)
        if N >> 1 << 1 == N:
            return res
        # print(s, a, b)
        for ii in range(1, N):
            # ss = s[ii:] + s[:ii]
            a = dp[0] + (1 if s[ii - 1] == "0" else -1)
            b = dp[1] + (1 if s[ii - 1] == "1" else -1)
            dp = [b, a]
            res = min(res, b, a)
            # print(ss, b, a, change(ss))
        return res