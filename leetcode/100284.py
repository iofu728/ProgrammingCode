# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-05 12:49:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-05 12:49:12

"""
100284. 有效单词 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
有效单词 需要满足以下几个条件：

至少 包含 3 个字符。
由数字 0-9 和英文大小写字母组成。（不必包含所有这类字符。）
至少 包含一个 元音字母 。
至少 包含一个 辅音字母 。
给你一个字符串 word 。如果 word 是一个有效单词，则返回 true ，否则返回 false 。

注意：

'a'、'e'、'i'、'o'、'u' 及其大写形式都属于 元音字母 。
英文中的 辅音字母 是指那些除元音字母之外的字母。
 

示例 1：

输入：word = "234Adas"

输出：true

解释：

这个单词满足所有条件。

示例 2：

输入：word = "b3"

输出：false

解释：

这个单词的长度少于 3 且没有包含元音字母。

示例 3：

输入：word = "a3$e"

输出：false

解释：

这个单词包含了 '$' 字符且没有包含辅音字母。

 

提示：

1 <= word.length <= 20
word 由英文大写和小写字母、数字、'@'、'#' 和 '$' 组成。
"""
class Solution:
    def isValid(self, word: str) -> bool:
        N = len(word)
        if N < 3:
            return False
        if not any(ii in word.lower() for ii in "aeiou"):
            return False
        if not any(chr(ord("a") + ii) in word.lower() for ii in range(26) if chr(ord("a") + ii) not in "aeiou"):
            return False
        for ii in word:
            if not (ii in "0123456789" or ii.lower() in "".join([chr(ord("a") + ii) for ii in range(26)])):
                return False
        return True