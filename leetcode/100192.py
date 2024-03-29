# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-01-21 11:03:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-01-21 11:04:57

"""
100192. 输入单词需要的最少按键次数 II 显示英文描述 
通过的用户数9
尝试过的用户数10
用户总通过次数9
用户总提交次数10
题目难度Medium
给你一个字符串 word，由 不同 小写英文字母组成。

电话键盘上的按键与 不同 小写英文字母集合相映射，可以通过按压按键来组成单词。例如，按键 2 对应 ["a","b","c"]，我们需要按一次键来输入 "a"，按两次键来输入 "b"，按三次键来输入 "c"。

现在允许你将编号为 2 到 9 的按键重新映射到 不同 字母集合。每个按键可以映射到 任意数量 的字母，但每个字母 必须 恰好 映射到 一个 按键上。你需要找到输入字符串 word 所需的 最少 按键次数。

返回重新映射按键后输入 word 所需的 最少 按键次数。

下面给出了一种电话键盘上字母到按键的映射作为示例。注意 1，*，# 和 0 不 对应任何字母。


 

示例 1：


输入：word = "abcde"
输出：5
解释：图片中给出的重新映射方案的输入成本最小。
"a" -> 在按键 2 上按一次
"b" -> 在按键 3 上按一次
"c" -> 在按键 4 上按一次
"d" -> 在按键 5 上按一次
"e" -> 在按键 6 上按一次
总成本为 1 + 1 + 1 + 1 + 1 = 5 。
可以证明不存在其他成本更低的映射方案。
示例 2：


输入：word = "xyzxyzxyzxyz"
输出：12
解释：图片中给出的重新映射方案的输入成本最小。
"x" -> 在按键 2 上按一次
"y" -> 在按键 3 上按一次
"z" -> 在按键 4 上按一次
总成本为 1 * 4 + 1 * 4 + 1 * 4 = 12 。
可以证明不存在其他成本更低的映射方案。
注意按键 9 没有映射到任何字母：不必让每个按键都存在与之映射的字母，但是每个字母都必须映射到按键上。
示例 3：


输入：word = "aabbccddeeffgghhiiiiii"
输出：24
解释：图片中给出的重新映射方案的输入成本最小。
"a" -> 在按键 2 上按一次
"b" -> 在按键 3 上按一次
"c" -> 在按键 4 上按一次
"d" -> 在按键 5 上按一次
"e" -> 在按键 6 上按一次
"f" -> 在按键 7 上按一次
"g" -> 在按键 8 上按一次
"h" -> 在按键 9 上按两次
"i" -> 在按键 9 上按一次
总成本为 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24 。
可以证明不存在其他成本更低的映射方案。
 

提示：

1 <= word.length <= 105
word 仅由小写英文字母组成。
"""
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        idx, d = 0, 1
        res = 0
        for ii, jj in sorted(c.items(), key=lambda i:(-i[1])):
            idx += 1
            if idx > 8:
                idx = 1
                d += 1
            res += jj * d
        return res