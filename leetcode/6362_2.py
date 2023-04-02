# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-04-02 13:28:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-04-02 13:28:43
"""
6362. 最长平衡子字符串 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个仅由 0 和 1 组成的二进制字符串 s 。  

如果子字符串中 所有的 0 都在 1 之前 且其中 0 的数量等于 1 的数量，则认为 s 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。 

返回  s 中最长的平衡子字符串长度。

子字符串是字符串中的一个连续字符序列。

 

示例 1：

输入：s = "01000111"
输出：6
解释：最长的平衡子字符串是 "000111" ，长度为 6 。
示例 2：

输入：s = "00111"
输出：4
解释：最长的平衡子字符串是 "0011" ，长度为  4 。
示例 3：

输入：s = "111"
输出：0
解释：除了空子字符串之外不存在其他平衡子字符串，所以答案为 0 。
 

提示：

1 <= s.length <= 50
'0' <= s[i] <= '1'
"""


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        a, b = 0, 0
        res = 0
        idx = 0
        while idx < len(s):
            while idx < len(s) and s[idx] == "1":
                idx += 1
            a = 0
            while idx < len(s) and s[idx] == "0":
                a += 1
                idx += 1
            b = 0
            while idx < len(s) and s[idx] == "1":
                b += 1
                idx += 1
            res = max(res, min(a, b) * 2)

        return res
