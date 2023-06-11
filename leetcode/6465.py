# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-11 13:11:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-11 13:11:37

"""
6465. 执行子串操作后的字典序最小字符串 显示英文描述 
通过的用户数519
尝试过的用户数861
用户总通过次数519
用户总提交次数1387
题目难度Medium
给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以完成以下行为：

选则 s 的任一非空子字符串，可能是整个字符串，接着将字符串中的每一个字符替换为英文字母表中的前一个字符。例如，'b' 用 'a' 替换，'a' 用 'z' 替换。
返回执行上述操作 恰好一次 后可以获得的 字典序最小 的字符串。

子字符串 是字符串中的一个连续字符序列。

现有长度相同的两个字符串 x 和 字符串 y ，在满足 x[i] != y[i] 的第一个位置 i 上，如果  x[i] 在字母表中先于 y[i] 出现，则认为字符串 x 比字符串 y 字典序更小 。
 

示例 1：

输入：s = "cbabc"
输出："baabc"
解释：我们选择从下标 0 开始、到下标 1 结束的子字符串执行操作。 
可以证明最终得到的字符串是字典序最小的。
示例 2：

输入：s = "acbbc"
输出："abaab"
解释：我们选择从下标 1 开始、到下标 4 结束的子字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
示例 3：

输入：s = "leetcode"
输出："kddsbncd"
解释：我们选择整个字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
 

提示：

1 <= s.length <= 3 * 105
s 仅由小写英文字母组成

"""
class Solution:
    def smallestString(self, s: str) -> str:
        res = list(s)
        idx = 0
        N = len(s)
        while idx < N and s[idx] == "a":
            idx += 1
            
        if idx == N:
            res[-1] = "z"
        while idx < N and s[idx] != "a":
            res[idx] = chr(ord(s[idx]) - 1)
            idx += 1
            
        return "".join(res)