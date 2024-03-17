# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-03-17 12:28:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-03-17 12:28:33

"""
100248. 字符串及其反转中是否存在同一子字符串 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个字符串 s ，请你判断字符串 s 是否存在一个长度为 2 的子字符串，在其反转后的字符串中也出现。

如果存在这样的子字符串，返回 true；如果不存在，返回 false 。

 

示例 1：

输入：s = "leetcode"

输出：true

解释：子字符串 "ee" 的长度为 2，它也出现在 reverse(s) == "edocteel" 中。

示例 2：

输入：s = "abcba"

输出：true

解释：所有长度为 2 的子字符串 "ab"、"bc"、"cb"、"ba" 也都出现在 reverse(s) == "abcba" 中。

示例 3：

输入：s = "abcd"

输出：false

解释：字符串 s 中不存在满足「在其反转后的字符串中也出现」且长度为 2 的子字符串。

 

提示：

1 <= s.length <= 100
字符串 s 仅由小写英文字母组成。
"""
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        N = len(s)
        ss = s[::-1]
        for ii in range(N - 1):
            tmp = s[ii:ii+2]
            # print(tmp)
            if tmp in ss:
                return True
        return False