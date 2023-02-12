# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-02-12 12:00:45
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-02-12 12:04:44

"""
6357. 最少得分子序列 显示英文描述 
通过的用户数52
尝试过的用户数115
用户总通过次数54
用户总提交次数216
题目难度Hard
给你两个字符串 s 和 t 。

你可以从字符串 t 中删除任意数目的字符。

如果没有从字符串 t 中删除字符，那么得分为 0 ，否则：

令 left 为删除字符中的最小下标。
令 right 为删除字符中的最大下标。
字符串的得分为 right - left + 1 。

请你返回使 t 成为 s 子序列的最小得分。

一个字符串的 子序列 是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说 "ace" 是 "abcde" 的子序列，但是 "aec" 不是）。

 

示例 1：

输入：s = "abacaba", t = "bzaa"
输出：1
解释：这个例子中，我们删除下标 1 处的字符 "z" （下标从 0 开始）。
字符串 t 变为 "baa" ，它是字符串 "abacaba" 的子序列，得分为 1 - 1 + 1 = 1 。
1 是能得到的最小得分。
示例 2：

输入：s = "cde", t = "xyz"
输出：3
解释：这个例子中，我们将下标为 0， 1 和 2 处的字符 "x" ，"y" 和 "z" 删除（下标从 0 开始）。
字符串变成 "" ，它是字符串 "cde" 的子序列，得分为 2 - 0 + 1 = 3 。
3 是能得到的最小得分。
 

提示：

1 <= s.length, t.length <= 105
s 和 t 都只包含小写英文字母。

"""


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        N, M = len(s), len(t)

        @cache
        def is_ok(x, y):
            if x + y == 0:
                return True

            def get_x(idx):
                return t[idx] if idx < x else t[idx - x + M - y]

            idx = 0
            for ii in s:
                if ii == get_x(idx):
                    idx += 1
                    if idx >= x + y:
                        return True
            return False

        res = M
        last = M
        x = 0
        while x <= M:
            # for x in range(0, M + 1):
            l, r = 1, last + 1
            while l < r:
                m = (l + r) // 2
                if is_ok(x, m):
                    l = m + 1
                else:
                    r = m
            # print(x, l, r)
            l -= 1
            # print(x, l)

            # print(x, l, M)
            f = M - x - l <= res
            if is_ok(x, l):
                res = min(res, M - x - l)
            if l == 0:
                break
            if l == last or x == 0:
                x += 1
            else:
                x += last - l
            # print(x, last, l)
            last = min(l, M - x)

        l, r = x, M + 1
        while l < r:
            m = (l + r) // 2
            if is_ok(m, 0):
                l = m + 1
            else:
                r = m
        l -= 1
        if is_ok(l, 0):
            res = min(res, M - l)
        return res


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        s = " " + s
        t = " " + t
        pre = [0] * (n + 2)
        suf = [0] * (n + 2)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1]
            if pre[i] < m and s[i] == t[pre[i] + 1]:
                pre[i] += 1
        suf[n + 1] = m + 1
        for i in range(n, 0, -1):
            suf[i] = suf[i + 1]
            if suf[i] > 1 and s[i] == t[suf[i] - 1]:
                suf[i] -= 1
        res = m
        for i in range(n + 1):
            res = min(res, suf[i + 1] - pre[i] - 1)
        return max(res, 0)
