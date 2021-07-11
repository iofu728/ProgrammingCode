# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-07-11 12:30:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-07-11 12:31:11
"""
5809. 长度为 3 的不同回文子序列 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。

即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。

回文 是正着读和反着读一样的字符串。

子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。

例如，"ace" 是 "abcde" 的一个子序列。
 

示例 1：

输入：s = "aabca"
输出：3
解释：长度为 3 的 3 个回文子序列分别是：
- "aba" ("aabca" 的子序列)
- "aaa" ("aabca" 的子序列)
- "aca" ("aabca" 的子序列)
示例 2：

输入：s = "adc"
输出：0
解释："adc" 不存在长度为 3 的回文子序列。
示例 3：

输入：s = "bbcbaba"
输出：4
解释：长度为 3 的 4 个回文子序列分别是：
- "bbb" ("bbcbaba" 的子序列)
- "bcb" ("bbcbaba" 的子序列)
- "bab" ("bbcbaba" 的子序列)
- "aba" ("bbcbaba" 的子序列)
 

提示：

3 <= s.length <= 105
s 仅由小写英文字母组成
"""
import bisect


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        c = defaultdict(list)
        for ii, jj in enumerate(s):
            c[jj].append(ii)
        res = 0
        for ii, jj in c.items():
            if len(jj) >= 3:
                res += 1
            if len(jj) < 2:
                continue
            l, r = jj[0], jj[-1]
            for mm, nn in c.items():
                if mm == ii:
                    continue
                b_idx = bisect.bisect_left(nn, l)
                e_idx = bisect.bisect_right(nn, r)
                if b_idx != e_idx:
                    res += 1
        return res