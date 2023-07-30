# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-07-30 12:37:52
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-07-30 12:38:02

"""
6918. 包含三个字符串的最短字符串 显示英文描述 
通过的用户数16
尝试过的用户数45
用户总通过次数16
用户总提交次数78
题目难度Medium
给你三个字符串 a ，b 和 c ， 你的任务是找到长度 最短 的字符串，且这三个字符串都是它的 子字符串 。
如果有多个这样的字符串，请你返回 字典序最小 的一个。

请你返回满足题目要求的字符串。

注意：

两个长度相同的字符串 a 和 b ，如果在第一个不相同的字符处，a 的字母在字母表中比 b 的字母 靠前 ，那么字符串 a 比字符串 b 字典序小 。
子字符串 是一个字符串中一段连续的字符序列。
 

示例 1：

输入：a = "abc", b = "bca", c = "aaa"
输出："aaabca"
解释：字符串 "aaabca" 包含所有三个字符串：a = ans[2...4] ，b = ans[3..5] ，c = ans[0..2] 。结果字符串的长度至少为 6 ，且"aaabca" 是字典序最小的一个。
示例 2：

输入：a = "ab", b = "ba", c = "aba"
输出："aba"
解释：字符串 "aba" 包含所有三个字符串：a = ans[0..1] ，b = ans[1..2] ，c = ans[0..2] 。由于 c 的长度为 3 ，结果字符串的长度至少为 3 。"aba" 是字典序最小的一个。
 

提示：

1 <= a.length, b.length, c.length <= 100
a ，b ，c 只包含小写英文字母。
"""
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        @lru_cache(None)
        def get_same(x, y):
            N, M = len(x), len(y)
            z = min(N, M)
            if y in x:
                return z
            while z > 0:
                if x[N - z:] == y[:z]:
                    return z
                z -= 1
            return 0
        a, b, c = sorted([a, b, c])
        res, res_n = None, 10 ** 7
        for i, j, k in permutations([a, b, c], 3):
            ij = get_same(i, j)
            ij_s = i + j[ij:]
            ijk = get_same(ij_s, k)
            ijk_s = ij_s + k[ijk:]
            if len(ijk_s) < res_n or (len(ijk_s) == res_n and ijk_s < res):
                res = ijk_s
                res_n = len(ijk_s)
        return res
            
            
                