# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-07-14 10:55:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-07-14 10:55:51

"""
100352. 交换后字典序最小的字符串 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个仅由数字组成的字符串 s，在最多交换一次 相邻 且具有相同 奇偶性 的数字后，返回可以得到的字典序最小的字符串。

如果两个数字都是奇数或都是偶数，则它们具有相同的奇偶性。例如，5 和 9、2 和 4 奇偶性相同，而 6 和 9 奇偶性不同。

 

示例 1：

输入： s = "45320"

输出： "43520"

解释：

s[1] == '5' 和 s[2] == '3' 都具有相同的奇偶性，交换它们可以得到字典序最小的字符串。

示例 2：

输入： s = "001"

输出： "001"

解释：

无需进行交换，因为 s 已经是字典序最小的。

 

提示：

2 <= s.length <= 100
s 仅由数字组成。
"""
class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        N = len(s)
        for ii in range(N - 1):
            if s[ii] > s[ii + 1] and int(s[ii]) % 2 == int(s[ii + 1]) % 2:
                s[ii], s[ii + 1] = s[ii + 1], s[ii]
                break
        return "".join(s)
        