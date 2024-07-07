# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-07-07 11:47:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-07-07 11:47:52

"""
100328. 生成不含相邻零的二进制字符串 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个正整数 n。

如果一个二进制字符串 x 的所有长度为 2 的子字符串中包含 至少 一个 "1"，则称 x 是一个 有效 字符串。

返回所有长度为 n 的 有效 字符串，可以以任意顺序排列。

 

示例 1：

输入： n = 3

输出： ["010","011","101","110","111"]

解释：

长度为 3 的有效字符串有："010"、"011"、"101"、"110" 和 "111"。

示例 2：

输入： n = 1

输出： ["0","1"]

解释：

长度为 1 的有效字符串有："0" 和 "1"。

 

提示：

1 <= n <= 18
"""
class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ["0", "1"]
        for ii in range(n - 1):
            tmp = []
            for jj in res:
                tmp.append(jj + "1")
                if jj[-1] == "1":
                    tmp.append(jj + "0")
            res = tmp
        return res
                    