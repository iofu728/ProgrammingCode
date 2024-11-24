# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-11-24 13:51:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-11-24 13:51:38

"""
100445. 重排子字符串以形成目标字符串 显示英文描述 
通过的用户数308
尝试过的用户数354
用户总通过次数312
用户总提交次数424
题目难度Medium
给你两个字符串 s 和 t（它们互为字母异位词），以及一个整数 k。

你的任务是判断是否可以将字符串 s 分割成 k 个等长的子字符串，然后重新排列这些子字符串，并以任意顺序连接它们，使得最终得到的新字符串与给定的字符串 t 相匹配。

如果可以做到，返回 true；否则，返回 false。

字母异位词 是指由另一个单词或短语的所有字母重新排列形成的单词或短语，使用所有原始字母恰好一次。

子字符串 是字符串中的一个连续 非空 字符序列。

 

示例 1：

输入： s = "abcd", t = "cdab", k = 2

输出： true

解释：

将 s 分割成 2 个长度为 2 的子字符串：["ab", "cd"]。
重新排列这些子字符串为 ["cd", "ab"]，然后连接它们得到 "cdab"，与 t 相匹配。
示例 2：

输入： s = "aabbcc", t = "bbaacc", k = 3

输出： true

解释：

将 s 分割成 3 个长度为 2 的子字符串：["aa", "bb", "cc"]。
重新排列这些子字符串为 ["bb", "aa", "cc"]，然后连接它们得到 "bbaacc"，与 t 相匹配。
示例 3：

输入： s = "aabbcc", t = "bbaacc", k = 2

输出： false

解释：

将 s 分割成 2 个长度为 3 的子字符串：["aab", "bcc"]。
这些子字符串无法重新排列形成 t = "bbaacc"，所以输出 false。
 

提示：

1 <= s.length == t.length <= 2 * 105
1 <= k <= s.length
s.length 能被 k 整除。
s 和 t 仅由小写英文字母组成。
输入保证 s 和 t 互为字母异位词。
"""
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        N = len(s)
        e = N // k
        c = Counter([s[ii: ii + e] for ii in range(0, N, e)])
        for ii in range(0, N, e):
            now = t[ii: ii + e]
            if c[now] == 0:
                return False
            c[now] -= 1
        return True
        