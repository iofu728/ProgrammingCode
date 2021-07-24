# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-07-24 22:30:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-07-24 23:19:18
"""
5804. 检查是否所有字符出现次数相同 显示英文描述 
通过的用户数2093
尝试过的用户数2126
用户总通过次数2123
用户总提交次数2646
题目难度Easy
给你一个字符串 s ，如果 s 是一个 好 字符串，请你返回 true ，否则请返回 false 。

如果 s 中出现过的 所有 字符的出现次数 相同 ，那么我们称字符串 s 是 好 字符串。

 

示例 1：

输入：s = "abacbc"
输出：true
解释：s 中出现过的字符为 'a'，'b' 和 'c' 。s 中所有字符均出现 2 次。
示例 2：

输入：s = "aaabb"
输出：false
解释：s 中出现过的字符为 'a' 和 'b' 。
'a' 出现了 3 次，'b' 出现了 2 次，两者出现次数不同。
 

提示：

1 <= s.length <= 1000
s 只包含小写英文字母。
"""


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = collections.Counter(s)
        return len(set(c.values())) == 1