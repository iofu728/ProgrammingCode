# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-13 11:15:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-13 12:22:49

"""
5514. 检查字符串是否可以通过排序子字符串得到另一个字符串 显示英文描述 
通过的用户数87
尝试过的用户数196
用户总通过次数88
用户总提交次数286
题目难度Hard
给你两个字符串 s 和 t ，请你通过若干次以下操作将字符串 s 转化成字符串 t ：

选择 s 中一个 非空 子字符串并将它包含的字符就地 升序 排序。
比方说，对下划线所示的子字符串进行操作可以由 "14234" 得到 "12344" 。

如果可以将字符串 s 变成 t ，返回 true 。否则，返回 false 。

一个 子字符串 定义为一个字符串中连续的若干字符。

 

示例 1：

输入：s = "84532", t = "34852"
输出：true
解释：你可以按以下操作将 s 转变为 t ：
"84532" （从下标 2 到下标 3）-> "84352"
"84352" （从下标 0 到下标 2） -> "34852"
示例 2：

输入：s = "34521", t = "23415"
输出：true
解释：你可以按以下操作将 s 转变为 t ：
"34521" -> "23451"
"23451" -> "23415"
示例 3：

输入：s = "12345", t = "12435"
输出：false
示例 4：

输入：s = "1", t = "2"
输出：false
 

提示：

s.length == t.length
1 <= s.length <= 105
s 和 t 都只包含数字字符，即 '0' 到 '9' 。
"""

from collections import Counter, defaultdict


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        def get_rc(ss: str):
            rc, c = defaultdict(int), Counter()
            for ii in ss:
                now = int(ii)
                for jj in range(now + 1, 10):
                    if c[jj]:
                        rc[(now, jj)] += c[jj]
                print(rc, c)
                c[now] += 1
            return rc

        cs, ct = Counter(s), Counter(t)
        for ii in "0123456789":
            if cs[ii] != ct[ii]:
                return False
        if s < t:
            return False
        if s == t:
            return True
        rcs, rct = get_rc(s), get_rc(t)
        for ii in rcs:
            if rct[ii] > rcs[ii]:
                return False
        return True

