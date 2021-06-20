# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-06-20 11:41:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-20 11:41:29

"""
5788. 字符串中的最大奇数 显示英文描述 
通过的用户数14
尝试过的用户数15
用户总通过次数14
用户总提交次数15
题目难度Easy
给你一个字符串 num ，表示一个大整数。请你在字符串 num 的所有 非空子字符串 中找出 值最大的奇数 ，并以字符串形式返回。如果不存在奇数，则返回一个空字符串 "" 。

子字符串 是字符串中的一个连续的字符序列。

 

示例 1：

输入：num = "52"
输出："5"
解释：非空子字符串仅有 "5"、"2" 和 "52" 。"5" 是其中唯一的奇数。
示例 2：

输入：num = "4206"
输出：""
解释：在 "4206" 中不存在奇数。
示例 3：

输入：num = "35427"
输出："35427"
解释："35427" 本身就是一个奇数。
 

提示：

1 <= num.length <= 105
num 仅由数字组成且不含前导零
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        N = len(num)
        idx = N - 1
        while idx >= 0 and int(num[idx]) >> 1 << 1 == int(num[idx]):
            idx -= 1
        return num[: idx + 1]
