# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-05 22:33:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-05 22:55:08


"""
5492. 分割字符串的方案数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个二进制串 s  （一个只包含 0 和 1 的字符串），我们可以将 s 分割成 3 个 非空 字符串 s1, s2, s3 （s1 + s2 + s3 = s）。

请你返回分割 s 的方案数，满足 s1，s2 和 s3 中字符 '1' 的数目相同。

由于答案可能很大，请将它对 10^9 + 7 取余后返回。

 

示例 1：

输入：s = "10101"
输出：4
解释：总共有 4 种方法将 s 分割成含有 '1' 数目相同的三个子字符串。
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
示例 2：

输入：s = "1001"
输出：0
示例 3：

输入：s = "0000"
输出：3
解释：总共有 3 种分割 s 的方法。
"0|0|00"
"0|00|0"
"00|0|0"
示例 4：

输入：s = "100100010100110"
输出：12
 

提示：

s[i] == '0' 或者 s[i] == '1'
3 <= s.length <= 10^5
"""


class Solution:
    MODS = 10 ** 9 + 7

    def numWays(self, s: str) -> int:
        def getC(a, b):
            res = 1
            if b > a >> 1:
                b = a - b
            for ii in range(a, a - b, -1):
                res *= ii
            for ii in range(2, b + 1):
                res /= ii
            return int(res) % self.MODS

        N = len(s)
        T3 = len([1 for ii in s if ii == "1"])
        if T3 % 3:
            return 0
        if not T3:
            return getC(N - 1, 2)
        b, e, num, idx = [], [], 0, 0
        while idx < N and num != (T3 // 3):
            num += s[idx] == "1"
            idx += 1
        b.append(idx - 1)
        while idx < N and s[idx] == "0":
            idx += 1
        e.append(idx)
        while idx < N and num != (T3 // 3) * 2:
            num += s[idx] == "1"
            idx += 1
        b.append(idx - 1)
        while idx < N and s[idx] == "0":
            idx += 1
        e.append(idx)
        res = 1
        for ii, jj in zip(b, e):
            res *= jj - ii
        return res % self.MODS

