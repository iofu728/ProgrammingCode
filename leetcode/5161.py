# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-07-18 13:10:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-07-18 13:10:42

"""
5161. 可以输入的最大单词数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。

给你一个由若干单词组成的字符串 text ，单词间由单个空格组成（不含前导和尾随空格）；另有一个字符串 brokenLetters ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 text 中单词的数目。

 

示例 1：

输入：text = "hello world", brokenLetters = "ad"
输出：1
解释：无法输入 "world" ，因为字母键 'd' 已损坏。
示例 2：

输入：text = "leet code", brokenLetters = "lt"
输出：1
解释：无法输入 "leet" ，因为字母键 'l' 和 't' 已损坏。
示例 3：

输入：text = "leet code", brokenLetters = "e"
输出：0
解释：无法输入任何单词，因为字母键 'e' 已损坏。
 

提示：

1 <= text.length <= 104
0 <= brokenLetters.length <= 26
text 由若干用单个空格分隔的单词组成，且不含任何前导和尾随空格
每个单词仅由小写英文字母组成
brokenLetters 由 互不相同 的小写英文字母组成
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        b = set(brokenLetters)

        def ok(s):
            for ii in s:
                if ii in b:
                    return False
            return True

        res = 0
        for ii in text.split():
            if ii and ok(ii):
                res += 1
        return res
